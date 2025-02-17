# Generated by Django 3.0.3 on 2020-02-18 22:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(help_text='Enter the pomodoro category', max_length=100)),
                ('categoryID', models.UUIDField(default=uuid.uuid4, help_text='Unique identifier for category', primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pomodoro',
            fields=[
                ('task_name', models.TextField(help_text='Enter task name for pomodoro')),
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular pomodoro across whole library', primary_key=True, serialize=False, unique=True)),
                ('day_of_week', models.CharField(help_text='Day of week (i.e. Monday-Sunday)', max_length=10)),
                ('time_of_day', models.DateTimeField(help_text='XX:XX AM or PM')),
                ('minutes', models.IntegerField(default=25)),
                ('categoryID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='timer.Category')),
            ],
        ),
    ]
