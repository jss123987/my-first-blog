# Generated by Django 3.0.3 on 2020-03-08 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_auto_20200308_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='caption',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
