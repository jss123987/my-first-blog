# Generated by Django 2.2.12 on 2020-06-06 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0079_auto_20200606_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trashphoto',
            name='x1',
        ),
        migrations.RemoveField(
            model_name='trashphoto',
            name='x2',
        ),
        migrations.RemoveField(
            model_name='trashphoto',
            name='y1',
        ),
        migrations.RemoveField(
            model_name='trashphoto',
            name='y2',
        ),
        migrations.AddField(
            model_name='post',
            name='x1',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='x2',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='y1',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='y2',
            field=models.FloatField(null=True),
        ),
    ]
