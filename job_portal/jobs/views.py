from django.shortcuts import render, redirect
from .forms import SignUpForm , JobForm , CustomUserLoginForm
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from .models import Job  # Keep this import for Job model
from .models import CustomUser
CustomUser = get_user_model()

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'jobs/signup.html', {'form': form})

def login_required_view(request):
    if request.user.is_authenticated:
        return True
    return False
def job_list_view(request):
     if not login_required_view(request):
        return redirect('login')
     jobs = Job.objects.all()
     return render(request, 'jobs/job_list.html', {'jobs': jobs})

def admin_dashboard_view(request):
    if not login_required_view(request):
        return redirect('login')
    if request.user.is_superuser:
        users = CustomUser.objects.all()
        return render(request, 'jobs/admin_dashboard.html', {'users': users})
    else:
        return redirect('login')
def add_job_view(request):
    if not login_required_view(request):
        return redirect('login')
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            return redirect('dashboard')
    else:
        form = JobForm()
    return render(request, 'jobs/add_job.html', {'form': form})
def success_view(request):
    return render(request, 'jobs/success.html')

def custom_login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_staff:  
                return redirect('admin_dashboard')
            else:
                return redirect('dashboard')
    else:
        form = CustomUserLoginForm()
    return render(request, 'jobs/login.html', {'form': form})
def home(request):
    return render(request, 'home.html')

def custom_logout(request):
    logout(request)  # Log out the user
    return redirect('login') 