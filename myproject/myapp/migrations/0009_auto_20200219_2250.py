# Generated by Django 3.0.3 on 2020-02-20 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_post_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subcategory',
            field=models.CharField(choices=[('World', 'World'), ('U.S.', 'U.S.')], default='U.S.', max_length=15),
        ),
    ]
