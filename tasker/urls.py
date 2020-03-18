from django.urls import path
from . import views, views_list, views_intl, rss

urlpatterns = [
    path('', views.TaskListView.as_view(), name='list'),
    path('<int:task_id>', views.show, name='task-show'),
    path('<int:task_id>/done', views.done, name='done'),
    path('new', views.create, name='new'),  # /task/new
    # списки тасков
    path('list/<int:list_id>', views_list.show, name='list-show'),
    path('list/new/<str:name>', views_list.add, name='list-new'),
    # интернационализация
    path('intl/today', views_intl.today),
    path('intl/hello', views_intl.hello),
    # rss
    path('rss', rss.TaskFeed())
]
