# Generated by Django 3.0.3 on 2020-02-20 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_post_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subcategory',
            field=models.CharField(choices=[('World', 'World'), ('U.S.', 'U.S.')], default='World', max_length=15),
        ),
    ]
