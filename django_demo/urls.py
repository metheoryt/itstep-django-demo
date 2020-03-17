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

urlpatterns = [
    u.path('admin/', admin.site.urls),
    u.path('task/', u.include('tasker.urls')),
    u.path('accounts/login/', views_auth.login_view),
    u.path('accounts/logout/', views_auth.logout),
    u.path('accounts/profile', views_auth.profile),
]
