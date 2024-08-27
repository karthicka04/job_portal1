from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [

    path('signup/', views.signup_view, name='register'),  # Registration page
    path('login/', views.custom_login, name='login'),  # Custom login view
    #path('logout/', views.custom_logout, name='logout'),  # Custom logout view
    path('dashboard/', views.job_list_view, name='dashboard'),  # User dashboard
    #path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'),  # Apply for a job
    path('admin_dashboard/', views.admin_dashboard_view, name='admin_dashboard'),  # Admin dashboard
    path('create_job/', views.add_job_view, name='create_job'),  # Create a job posting (for admin)
]
