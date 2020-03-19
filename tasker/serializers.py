from rest_framework import serializers as s
from .models import Task, TaskList, TaskMembership


class TaskSerializer(s.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['url', 'text']

    def create(self, validated_data):
        # создаёт от имени текущего пользователя
        validated_data['user'] = self.context['request'].user
        return Task.objects.create(**validated_data)


class TaskMembershipSerializer(s.HyperlinkedModelSerializer):
    class Meta:
        model = TaskMembership
        fields = ['url', 'position', 'task', 'list']


class TaskListSerializer(s.HyperlinkedModelSerializer):
    class Meta:
        model = TaskList
        fields = ['url', 'name']

    def create(self, validated_data):
        # создаёт от имени текущего пользователя
        validated_data['user'] = self.context['request'].user
        return TaskList.objects.create(**validated_data)
