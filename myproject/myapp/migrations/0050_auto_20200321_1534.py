# Generated by Django 3.0.3 on 2020-03-21 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0049_auto_20200320_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='p1',
            field=models.FileField(default='', upload_to='documents/'),
        ),
    ]
