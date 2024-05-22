# Generated by Django 4.2.13 on 2024-05-22 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0010_alter_machineslistpluginmodel_cmsplugin_ptr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='material',
            field=models.ManyToManyField(blank=True, to='machines.material'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='workshop',
            field=models.ManyToManyField(blank=True, to='machines.workshop'),
        ),
        migrations.AlterField(
            model_name='software',
            name='machines',
            field=models.ManyToManyField(blank=True, to='machines.machine'),
        ),
    ]
