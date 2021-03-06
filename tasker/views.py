from time import sleep

from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView
from .models import Task, TaskModelForm
import logging
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

log = logging.getLogger(__name__)


@login_required
def create(request):
    if request.method == 'GET':
        return render(request, 'form.html', context=dict(form=TaskModelForm()))
    elif request.method == 'POST':
        if not request.user.has_perm('tasker.add_task'):
            return HttpResponseForbidden()
        form = TaskModelForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect(show, task.id)
        else:
            return render(request, 'form.html', context=dict(form=form))


def update(request, task_id: int):
    """практическое задание за 12.03.
    обновляет существующую модель таска
    """
    pass


def show(request, task_id: int):
    log.info('show request')
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
