# Generated by Django 3.2.17 on 2023-02-02 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0002_alter_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
