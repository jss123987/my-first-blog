# Generated by Django 3.0.3 on 2020-03-25 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0064_auto_20200324_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='EmailAddress',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
