from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView

from .models import Task, User
from .forms import TaskForm


def add(request):
    if request.method == 'GET':
        return render(request, 'form_task.html', context=dict(form=TaskForm()))
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            user = User.objects.get(pk=1)
            task = Task(user=user, text=form.cleaned_data['text'])
            if form.cleaned_data['is_completed']:
                task.date_completed = timezone.now()
            task.save()
            return redirect(show, task.id)
        else:
            return render(request, 'form_task.html', context=dict(form=form))


def show(request, task_id: int):
    task = Task.objects.get(pk=task_id)
    return render(request, 'show.html', context={'task': task})


def done(request, task_id: int):
    task = Task.objects.get(pk=task_id)
    task.date_completed = timezone.now()
    task.save()
    return redirect(show, task.id)


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
