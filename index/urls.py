from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('projects/category/<int:pk>/', views.projects_category, name='projects_category'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service_list'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home_page'), name='logout'),
]