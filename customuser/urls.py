from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('registrations/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.AuthLogin.as_view(), name='login'),
    path('users/', views.Userlist.as_view(), name='user_list'),
]
