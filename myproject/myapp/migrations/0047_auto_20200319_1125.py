# Generated by Django 3.0.3 on 2020-03-19 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0046_auto_20200319_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='p10',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='p11',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='p12',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='p13',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='p8',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='p9',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
