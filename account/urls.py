from django.urls import path
from .views import register
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register', register, name='register'),
    path('login', obtain_auth_token, name='login')
]
