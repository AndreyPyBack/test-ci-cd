from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}  # Убедитесь, что пароль записываемый и не читаемый

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'bio', 'city']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        # Хеширование пароля перед сохранением
        user_data['password'] = make_password(user_data['password'])
        user = User.objects.create(**user_data)
        profile = Profile.objects.create(user=user, **validated_data)
        return profile


from rest_framework import serializers
from .models import Car  # Убедитесь, что импорт модели корректный

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'



from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  # Показываем имя пользователя вместо ID

    class Meta:
        model = Comment
        fields = ['id', 'product', 'user', 'text', 'created_at']
        read_only_fields = ['user']  # делаем поле user доступным только для чтения

    def create(self, validated_data):
        # Получаем пользователя из контекста запроса
        user = self.context['request'].user
        # Добавляем пользователя в validated_data
        validated_data['user'] = user
        # Создаем новый объект Comment
        return super().create(validated_data)


