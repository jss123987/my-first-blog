# Generated by Django 3.0.3 on 2020-03-21 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0050_auto_20200321_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='p1',
            field=models.FileField(blank=True, default='', upload_to='documents/'),
        ),
    ]
