from django import forms as f


class TaskForm(f.Form):
    text = f.CharField()
    is_completed = f.BooleanField(required=False)
