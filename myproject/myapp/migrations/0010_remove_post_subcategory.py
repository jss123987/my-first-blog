# Generated by Django 3.0.3 on 2020-02-20 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20200219_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='subcategory',
        ),
    ]
