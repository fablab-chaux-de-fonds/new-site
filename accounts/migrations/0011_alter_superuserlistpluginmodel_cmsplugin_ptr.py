# Generated by Django 4.2.11 on 2024-04-28 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        #('cms', '0036_alter_cmsplugin_id_alter_globalpagepermission_id_and_more'),
        ('accounts', '0010_auto_20230804_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superuserlistpluginmodel',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin'),
        ),
    ]
