from django.urls import path
from . import views


urlpatterns = [
    path('sign_up/', views.sign_up, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('submit/', views.submit, name='submit'),
    path('login/', views.login, name='login'),
]
