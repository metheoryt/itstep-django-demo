from django.contrib.syndication.views import Feed
from django.urls import reverse
from tasker.models import Task


class TaskFeed(Feed):
    title = "Tasks feed"
    link = "/task"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return Task.objects.order_by('-id')[:5]

    def item_title(self, item: Task):
        return item.text

    def item_description(self, item: Task):
        return item.text

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('task-show', kwargs=dict(task_id=item.pk))
