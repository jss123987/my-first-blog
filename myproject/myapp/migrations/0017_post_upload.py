# Generated by Django 3.0.3 on 2020-03-06 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_remove_post_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upload',
            field=models.FileField(blank=True, upload_to='myapp/static/img'),
        ),
    ]
