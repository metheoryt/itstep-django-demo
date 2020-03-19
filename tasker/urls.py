from django.urls import path, include
from . import views, views_list, views_intl, rss, views_api
from rest_framework import routers

api_router = routers.DefaultRouter()
api_router.register('tasks', views_api.TaskViewSet)
api_router.register('task-lists', views_api.TaskListViewSet)
api_router.register('task-list-memberships', views_api.TaskMembershipViewSet)

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
    path('rss', rss.TaskFeed()),
    # api
    path('api/', include(api_router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework'))
]
