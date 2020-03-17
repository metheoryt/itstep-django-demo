from django.shortcuts import render, redirect
from django.utils import timezone
from django.utils.translation import gettext as _
from django.http import HttpResponse


def hello(request):
    greeting = _('hello world!')
    return HttpResponse(greeting)


def today(request):
    now = timezone.now()
    content = _('Today is %(month)s %(day)d')  % {'month': now.strftime('%B'), 'day': now.day}
    return HttpResponse(content)
