from rest_framework import viewsets
from rest_framework import permissions
from . import serializers
from .models import Task, TaskList, TaskMembership


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_added')
    serializer_class = serializers.TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class TaskListViewSet(viewsets.ModelViewSet):
    queryset = TaskList.objects.all().order_by('-date_added')
    serializer_class = serializers.TaskListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
