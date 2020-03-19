from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from . import serializers
from .models import Task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_added')
    serializer_class = serializers.TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     return self.queryset.filter(user=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]
