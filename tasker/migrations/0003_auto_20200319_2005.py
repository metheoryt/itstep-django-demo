# Generated by Django 3.0.3 on 2020-03-19 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0002_article_reporter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklist',
            name='user',
        ),
        migrations.RemoveField(
            model_name='task',
            name='list',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Reporter',
        ),
        migrations.DeleteModel(
            name='TaskList',
        ),
    ]