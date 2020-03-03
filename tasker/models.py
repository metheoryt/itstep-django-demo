from django.db import models
from django.db.models import fields as f


class User(models.Model):
    login = f.TextField()


# Create your models here.
class Task(models.Model):
    text = f.TextField()
    date_added = f.DateTimeField(auto_now_add=True)
    date_completed = f.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
