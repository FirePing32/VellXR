# Generated by Django 2.1.5 on 2019-02-15 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20190215_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='slug',
        ),
    ]
