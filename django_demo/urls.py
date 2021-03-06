"""django_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import django.urls as u
from tasker import views_auth
from django.contrib.auth import views as auth_views
from django.conf import global_settings
from . import views


from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from tasker.models import Task

info_dict = {
    'queryset': Task.objects.all(),
    'date_field': 'date_added',
}


urlpatterns = [
    u.path('admin/', admin.site.urls),
    u.path('task/', u.include('tasker.urls')),
    u.path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html')),
    u.path('accounts/logout/', auth_views.LogoutView.as_view(template_name='logout.html')),
    u.path('accounts/profile/', views_auth.profile),
    u.path('now', views.now),
    u.path('email', views.email),
    # sitemap
    path('sitemap.xml', sitemap, {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
         name='django.contrib.sitemaps.views.sitemap'),
]
