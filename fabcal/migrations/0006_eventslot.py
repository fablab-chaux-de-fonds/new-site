# Generated by Django 3.2.13 on 2022-06-11 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('openings', '0005_event'),
        ('fabcal', '0005_openingslot_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('has_supcritions', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('price', models.CharField(max_length=255)),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openings.event')),
                ('subcriptions', models.ManyToManyField(related_name='event_subscriptions_users', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Event Slot',
                'verbose_name_plural': 'Event Slots',
            },
        ),
    ]
