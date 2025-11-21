from django.urls import path
from . import views


urlpatterns = [
    path('sign_up/', views.sign_up, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('submit/', views.submit, name='submit'),
]
