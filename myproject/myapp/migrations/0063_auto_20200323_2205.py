# Generated by Django 3.0.3 on 2020-03-24 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0062_auto_20200323_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='EmailAddress',
            field=models.CharField(max_length=40, null=True),
        ),
    ]