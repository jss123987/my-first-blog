# Generated by Django 3.0.3 on 2020-03-05 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200305_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='texts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.yo'),
        ),
    ]
