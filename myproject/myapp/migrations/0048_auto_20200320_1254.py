# Generated by Django 3.0.3 on 2020-03-20 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0047_auto_20200319_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='p1',
            field=models.FileField(blank=True, default='', upload_to='documents/'),
        ),
    ]
