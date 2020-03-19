from rest_framework import serializers as s
from django.contrib.auth.models import User
from .models import Task


class UserSerializer(s.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff']


class TaskSerializer(s.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['url', 'text', 'user']

    user = UserSerializer(read_only=True)

    def create(self, validated_data):
        # создаёт от имени текущего пользователя
        validated_data['user'] = self.context['request'].user
        return Task.objects.create(**validated_data)
