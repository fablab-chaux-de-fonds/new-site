# Generated by Django 3.2.20 on 2023-08-04 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0008_auto_20230803_2148'),
        ('accounts', '0009_superuserlistpluginmodel_superuserprofile_superuserstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superuserprofile',
            name='machine_category',
            field=models.ManyToManyField(blank=True, null=True, to='machines.MachineCategory', verbose_name='Machine category'),
        ),
        migrations.AlterField(
            model_name='superuserprofile',
            name='software',
            field=models.ManyToManyField(blank=True, null=True, to='machines.Software', verbose_name='Software'),
        ),
        migrations.AlterField(
            model_name='superuserprofile',
            name='status',
            field=models.ManyToManyField(blank=True, null=True, to='accounts.SuperUserStatus', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='superuserprofile',
            name='technique',
            field=models.ManyToManyField(blank=True, null=True, to='machines.Workshop', verbose_name='Technique'),
        ),
        migrations.AlterField(
            model_name='superuserprofile',
            name='trainer',
            field=models.ManyToManyField(blank=True, null=True, to='machines.Training', verbose_name='Trainer'),
        ),
    ]
