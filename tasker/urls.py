from django.urls import path
from . import views, list_views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='list'),
    path('<int:task_id>', views.show, name='task-show'),
    path('<int:task_id>/done', views.done, name='done'),
    path('new', views.add, name='new'),
    # списки тасков
    path('list/<int:list_id>', list_views.show, name='list-show'),
    path('list/new/<str:name>', list_views.add, name='list-new'),
    # 'list/{int:list_id}/add/{int:task_id}' - добавление таска в список
]
