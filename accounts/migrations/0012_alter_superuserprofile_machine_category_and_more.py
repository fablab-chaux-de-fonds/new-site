# Generated by Django 4.2.13 on 2024-05-22 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0011_alter_machine_material_alter_machine_workshop_and_more'),
        ('accounts', '0011_alter_superuserlistpluginmodel_cmsplugin_ptr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superuserprofile',
            name='machine_category',
            field=models.ManyToManyField(blank=True, to='machines.machinecategory', verbose_name='Machine category'),
        ),
        migrations.AlterField(
            model_name='superuserprofile',
            name='software',
            field=models.ManyToManyField(blank=True, to='machines.software', verbose_name='Software'),
        ),
        migrations.AlterField(
            model_name='superuserprofile',
            name='status',
            field=models.ManyToManyField(blank=True, to='accounts.superuserstatus', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='superuserprofile',
            name='technique',
            field=models.ManyToManyField(blank=True, to='machines.workshop', verbose_name='Technique'),
        ),
        migrations.AlterField(
            model_name='superuserprofile',
            name='trainer',
            field=models.ManyToManyField(blank=True, to='machines.training', verbose_name='Trainer'),
        ),
    ]
