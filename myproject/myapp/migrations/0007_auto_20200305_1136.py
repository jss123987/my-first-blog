# Generated by Django 3.0.3 on 2020-03-05 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20200305_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yo',
            name='texts',
            field=models.CharField(max_length=200),
        ),
    ]