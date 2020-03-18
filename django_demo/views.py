from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import HttpResponse, HttpRequest
from datetime import datetime
from tasker.forms import EmailForm
from django.core.mail import send_mail


@cache_page(60)
def now(request):
    return HttpResponse(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def email(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'form.html', context={'form': EmailForm()})
    elif request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            payload = dict(
                subject=form.cleaned_data['subject'],
                from_email=form.cleaned_data['from_'],
                recipient_list=[form.cleaned_data['to']]
            )
            if '<' in form.cleaned_data['message']:
                payload['html_message'] = form.cleaned_data['message']
            else:
                payload['message'] = form.cleaned_data['message']
            send_mail(**payload)
        return HttpResponse('email was sent!')
