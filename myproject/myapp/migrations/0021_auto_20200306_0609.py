# Generated by Django 3.0.3 on 2020-03-06 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_auto_20200306_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upload',
            field=models.FileField(blank=True, upload_to='../../static/img/'),
        ),
    ]
