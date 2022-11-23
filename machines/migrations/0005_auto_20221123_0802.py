# Generated by Django 3.2.16 on 2022-11-23 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0004_auto_20221120_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='machines.machinecategory'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='machines.machinegroup'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='material',
            field=models.ManyToManyField(blank=True, null=True, to='machines.Material'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='workshop',
            field=models.ManyToManyField(blank=True, null=True, to='machines.Workshop'),
        ),
    ]
