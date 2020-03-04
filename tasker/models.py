from django.db import models
from django.db.models import fields as f


class User(models.Model):
    login = f.TextField()


class Task(models.Model):
    text = f.TextField()
    date_added = f.DateTimeField(auto_now_add=True)
    date_completed = f.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class TaskMembership(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    list = models.ForeignKey('TaskList', on_delete=models.CASCADE)
    position = models.IntegerField()


class TaskList(models.Model):
    date_added = f.DateTimeField(auto_now_add=True)
    name = f.CharField(max_length=100)
    tasks = models.ManyToManyField(Task, through=TaskMembership, related_name='lists')

    def __str__(self):
        return self.name
