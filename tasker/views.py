from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

from .models import Task


def add(request, text):
    task = Task(text=text)
    task.save()
    return redirect(show, task.id)


def show(request, task_id: int):
    task = Task.objects.get(pk=task_id)
    return render(request, 'show.html', context={'task': task})


def done(request, task_id: int):
    task = Task.objects.get(pk=task_id)
    task.date_completed = timezone.now()
    task.save()
    return redirect(show, task.id)
