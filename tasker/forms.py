from django import forms as f
from django.forms import widgets as w


class TaskForm(f.Form):
    text = f.CharField(max_length=10, label='Таск', help_text='что вы хотите сделать?')
    is_completed = f.BooleanField(required=False, label='Завершено', label_suffix='?')
