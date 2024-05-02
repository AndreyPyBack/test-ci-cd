from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ProtectedView(APIView):
    # Требует аутентификации
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World! Это закрытая '}
        return Response(content)

class OpenView(APIView):
    # Доступно без аутентификации
    permission_classes = []

    def get(self, request):
        content = {'message': 'Hello, World! Это открытая '}
        return Response(content)

from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .serializers import ProfileSerializer
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            data = {
                "user_id": user.id,
                "message": "User registered successfully."
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from .models import Car
from .serializers import CarSerializer

class ApiCarDetail(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

from rest_framework import permissions
from .permissions import IsEditor

class CarDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsEditor]  # Применяем разрешение IsEditor


from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer

from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer

class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        # Установить пользователя, отправившего запрос, как автора комментария
        serializer.save(user=self.request.user)
