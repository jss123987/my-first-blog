# Generated by Django 3.0.3 on 2020-03-21 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0051_auto_20200321_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='p1',
            field=models.FileField(default='', null=True, upload_to='documents/'),
        ),
    ]
