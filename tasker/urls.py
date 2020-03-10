from django.urls import path
from . import views

urlpatterns = [
    path('<int:task_id>', views.show, name='show'),
    path('<int:task_id>/done', views.done, name='done'),
    path('new/<str:text>', views.add, name='new'),
    path('', views.TaskListView.as_view(), name='list'),
]
