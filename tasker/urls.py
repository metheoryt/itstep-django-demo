from django.urls import path, include
from . import views, views_intl, rss, views_api
from rest_framework import routers

api_router = routers.DefaultRouter()
api_router.register('tasks', views_api.TaskViewSet)  # /task/api/tasks
api_router.register('users', views_api.UserViewSet)  # /task/api/users

urlpatterns = [
    path('', views.TaskListView.as_view(), name='list'),
    path('<int:task_id>', views.show, name='task-show'),
    path('<int:task_id>/done', views.done, name='done'),
    path('new', views.create, name='new'),  # /task/new
    # интернационализация
    path('intl/today', views_intl.today),
    path('intl/hello', views_intl.hello),
    # rss
    path('rss', rss.TaskFeed()),
    # api
    path('api/', include(api_router.urls)),  # /task/api/
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework'))  # /task/api/auth/
]
