from django.urls import path
from . import views

urlpatterns = [
    path('<int:task_id>', views.show),
    path('<int:task_id>/done', views.done),
    path('new/<str:text>', views.add),
]
