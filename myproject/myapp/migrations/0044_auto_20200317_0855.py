# Generated by Django 3.0.3 on 2020-03-17 12:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0043_auto_20200317_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contributers',
            field=models.ManyToManyField(blank=True, related_name='contributers', to=settings.AUTH_USER_MODEL),
        ),
    ]
