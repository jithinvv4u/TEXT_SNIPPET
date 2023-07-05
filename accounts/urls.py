from django.contrib import admin
from django.urls import path, include
from .views import LoginView, RefreshView, RegistrationView

urlpatterns = [
    path('signup/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', RefreshView.as_view(), name='token_refresh'),
]