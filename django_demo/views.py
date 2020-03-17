from django.views.decorators.cache import cache_page
from django.http import HttpResponse
from datetime import datetime


@cache_page(60)
def now(request):
    return HttpResponse(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
