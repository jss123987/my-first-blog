# Generated by Django 3.0.3 on 2020-03-07 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_auto_20200307_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upload',
            field=models.FileField(blank=True, upload_to='myapp/media/documents/'),
        ),
    ]