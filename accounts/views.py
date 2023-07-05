from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer, LoginSerializer, RefreshSerializer
# Create your views here.


class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class RefreshView(TokenRefreshView):
    serializer_class = RefreshSerializer