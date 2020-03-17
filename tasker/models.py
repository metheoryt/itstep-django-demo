from django.db import models
from django.db.models import fields as f
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Task(models.Model):
    class Meta:
        verbose_name = _('task')
        verbose_name_plural = _('tasks')

    text = f.TextField(_('text'), help_text=_('what to do'))
    date_added = f.DateTimeField(auto_now_add=True)
    date_completed = f.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class TaskModelForm(ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'user']


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
