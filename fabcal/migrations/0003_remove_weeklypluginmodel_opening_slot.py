# Generated by Django 3.2.13 on 2022-05-30 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fabcal', '0002_weeklypluginmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weeklypluginmodel',
            name='opening_slot',
        ),
    ]
