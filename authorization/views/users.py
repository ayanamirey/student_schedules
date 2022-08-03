from authorization.serializers.users import MyTokenObtainPairSerializer, RegisterSerializer
from authorization.models.users import MyUser
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
