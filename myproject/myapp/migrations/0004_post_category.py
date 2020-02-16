# Generated by Django 3.0.3 on 2020-02-15 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('arch', 'Archeology'), ('news', 'World News'), ('sci', 'Science'), ('celeb', 'Celebrity')], default='arch', max_length=5),
        ),
    ]
