from django.db import models
from django.db.models import fields as f


# Create your models here.
class Task(models.Model):
    text = f.TextField()
    date_added = f.DateTimeField(auto_now_add=True)
    date_completed = f.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'<Task #{self.id} "{self.text}">'
