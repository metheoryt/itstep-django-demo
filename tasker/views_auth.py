from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import logging

log = logging.getLogger(__name__)

# логин
# логаут
# проверка аутентификации


@login_required
def profile(request):
    log.info('profile requested')
    return HttpResponse(f'You are {request.user.username}')


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', '/'))
        else:
            return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/')
