from django.test import TestCase
from tasker.models import Task
from django.contrib.auth.models import User


# Create your tests here.
class TestTask(TestCase):

    def setUp(self):
        self.superuser: User = User.objects.create_superuser('su', password='123')
        self.user: User = User.objects.create_user('me', password='lol')
        self.task: Task = Task.objects.create(text='todo 1', user=self.user, list=self.user_list)

    def test_task_show_view(self):
        rv = self.client.get('/task/1')
        self.assertEqual(rv.status_code, 200)
        self.assertContains(rv, 'todo 1')
        self.assertEqual(rv.context['task'], self.task)

    def test_task_create_require_login(self):
        rv = self.client.get('/task/new')
        self.assertEqual(rv.status_code, 302)
        self.assertEqual(rv.url, '/accounts/login/?next=/task/new')

    def test_task_create_require_permission(self):
        self.client.login(username='me', password='lol')
        rv = self.client.post('/task/new', {'text': 'foo', 'user': self.user.id})
        self.assertEqual(rv.status_code, 403)

    def test_task_create_success(self):
        self.client.login(username='su', password='123')
        rv = self.client.post('/task/new', {'text': 'foo', 'user': self.superuser.id})
        self.assertEqual(rv.status_code, 302)
        self.assertEqual(rv.url, '/task/2')
