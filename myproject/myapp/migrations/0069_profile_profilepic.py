# Generated by Django 3.0.3 on 2020-03-25 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0068_auto_20200324_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profilepic',
            field=models.FileField(default='f', upload_to='documents/'),
        ),
    ]