from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView

from authentication.models import User
from authentication.serializer import UserDetailSerializer, SignupSerializer

# Create your views here.

class UserViewset(ModelViewSet):

    serializer_class = UserDetailSerializer

    def get_queryset(self):
        return User.objects.all()


class SignupView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
