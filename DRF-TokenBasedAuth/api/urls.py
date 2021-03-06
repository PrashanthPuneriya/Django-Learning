from django.urls import path
from .views import TestAPI, RegisterAPI, LoginAPI, ChangePassword
from rest_framework.authtoken import views as vw

app_name = 'api'

urlpatterns = [
    path('', TestAPI.as_view(), name='test-API'),
    
    path('register/', RegisterAPI.as_view(), name='register-API'),

    path('api-token-auth/', vw.obtain_auth_token, name='api-token-auth-API'), # To obtain token
    path('login/', LoginAPI.as_view(), name='loginAPI'), #Custom implementation of api-token-auth - IT just implements the above view

    path('change-password/', ChangePassword.as_view(), name='change-password-API')
]