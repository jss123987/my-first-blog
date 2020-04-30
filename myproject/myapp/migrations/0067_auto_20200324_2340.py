# Generated by Django 3.0.3 on 2020-03-25 03:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0066_auto_20200324_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='EmailAddress',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emaail', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usrname', to=settings.AUTH_USER_MODEL),
        ),
    ]