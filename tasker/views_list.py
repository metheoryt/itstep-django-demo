from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView


from .models import Task, User, TaskList


def show(request, list_id: int):
    list = TaskList.objects.get(pk=list_id)
    return render(request, 'list/show.html', context={'list': list})


def add(request, name: str):
    try:
        list = TaskList.objects.get(name=name)
    except TaskList.DoesNotExist:
        list = TaskList(name=name)
        list.save()

    return redirect(show, list.id)
