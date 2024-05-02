from django.urls import path
from .views import ProtectedView, OpenView, UserRegistrationView, ApiCarDetail, CarDetailView, CommentCreateAPIView

urlpatterns = [
    path('comments/create/', CommentCreateAPIView.as_view(), name='create-comment'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('open/', OpenView.as_view(), name='open'),
    path('register/',UserRegistrationView.as_view()),
    path('cars/<int:pk>/', ApiCarDetail.as_view(), name='car-detail'),
    path('cars1putpach/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
]
