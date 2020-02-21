# Generated by Django 3.0.3 on 2020-02-21 00:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timer', '0002_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='pomodoro',
            name='doer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
