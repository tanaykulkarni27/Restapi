# Generated by Django 4.0.6 on 2022-07-14 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_blogpost_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='user',
        ),
    ]