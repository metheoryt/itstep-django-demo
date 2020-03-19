from django.apps import AppConfig


class TaskerConfig(AppConfig):
    name = 'tasker'

    def ready(self):
        from tasker import signals
