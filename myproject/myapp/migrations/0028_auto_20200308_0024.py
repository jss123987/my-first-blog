# Generated by Django 3.0.3 on 2020-03-08 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_auto_20200307_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upload',
            field=models.FileField(default='', upload_to='documents/'),
        ),
    ]
