# Generated by Django 3.2.16 on 2022-11-16 20:44

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    replaces = [('machines', '0006_auto_20221015_0954'), ('machines', '0007_remove_tool_about'), ('machines', '0008_auto_20221015_1032'), ('machines', '0009_training_notification'), ('machines', '0010_auto_20221015_1845'), ('machines', '0011_auto_20221016_2100'), ('machines', '0012_auto_20221016_2147'), ('machines', '0013_rename_user_trainingvalidation_profile'), ('machines', '0014_auto_20221023_1808'), ('machines', '0015_auto_20221029_1921'), ('machines', '0016_auto_20221030_1458'), ('machines', '0017_auto_20221030_1516'), ('machines', '0018_auto_20221030_1528'), ('machines', '0019_auto_20221030_1638'), ('machines', '0020_auto_20221030_1730'), ('machines', '0021_auto_20221030_1758'), ('machines', '0022_alter_card_icon'), ('machines', '0023_card_url_resolver'), ('machines', '0024_remove_card_url_resolver'), ('machines', '0025_specification'), ('machines', '0026_auto_20221031_1918'), ('machines', '0027_remove_machine_spec'), ('machines', '0028_auto_20221116_2003')]

    dependencies = [
        ('machines', '0001_initial'),
        ('accounts', '0001_squashed_0006_alter_profile_public_contact_plateform'),
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tools',
            new_name='Tool',
        ),
        migrations.RenameModel(
            old_name='ToolsMachine',
            new_name='ToolMachine',
        ),
        migrations.RenameModel(
            old_name='ToolsTraining',
            new_name='ToolTraining',
        ),
        migrations.RemoveField(
            model_name='tool',
            name='about',
        ),
        migrations.RenameField(
            model_name='tool',
            old_name='href',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='itemforrent',
            old_name='price',
            new_name='full_price',
        ),
        migrations.RemoveField(
            model_name='itemforrent',
            name='description',
        ),
        migrations.RemoveField(
            model_name='itemforrent',
            name='title',
        ),
        migrations.CreateModel(
            name='TrainingValidation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machines.training')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machines.training')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MachinesListPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='machines_machineslistpluginmodel', serialize=False, to='cms.cmsplugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='tool',
            name='link_text',
            field=models.CharField(max_length=255, verbose_name='Text lien'),
        ),
        migrations.CreateModel(
            name='HighlightMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort', models.PositiveSmallIntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sort', models.PositiveSmallIntegerField(default=1)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Matière',
                'verbose_name_plural': 'Matières',
            },
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sort', models.PositiveSmallIntegerField(default=1)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Atelier',
                'verbose_name_plural': 'Ateliers',
            },
        ),
        migrations.RenameField(
            model_name='toolmachine',
            old_name='tool',
            new_name='card',
        ),
        migrations.RenameField(
            model_name='tooltraining',
            old_name='tool',
            new_name='card',
        ),
        migrations.RemoveField(
            model_name='machine',
            name='subscriber_price',
        ),
        migrations.RemoveField(
            model_name='machine',
            name='support',
        ),
        migrations.RemoveField(
            model_name='machine',
            name='visible',
        ),
        migrations.RemoveField(
            model_name='training',
            name='support',
        ),
        migrations.AddField(
            model_name='machine',
            name='premium_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Tarif membre'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machine',
            name='status',
            field=models.CharField(choices=[('hidden', 'Hidden'), ('available', 'Available'), ('maintenance', 'Maintenance')], default='available', max_length=255),
        ),
        migrations.AlterField(
            model_name='toolmachine',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machines.machine'),
        ),
        migrations.RenameModel(
            old_name='Tool',
            new_name='Card',
        ),
        migrations.DeleteModel(
            name='MachineTodoPoint',
        ),
        migrations.AddField(
            model_name='highlightmachine',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machines.card'),
        ),
        migrations.AddField(
            model_name='highlightmachine',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machines.machine'),
        ),
        migrations.RenameField(
            model_name='machinegroup',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='machine',
            name='sort',
        ),
        migrations.RemoveField(
            model_name='machinecategory',
            name='description',
        ),
        migrations.RemoveField(
            model_name='machinegroup',
            name='description',
        ),
        migrations.AddField(
            model_name='machinecategory',
            name='sort',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='machine',
            name='material',
            field=models.ManyToManyField(blank=True, to='machines.Material'),
        ),
        migrations.AddField(
            model_name='machine',
            name='workshop',
            field=models.ManyToManyField(blank=True, to='machines.Workshop'),
        ),
        migrations.RemoveField(
            model_name='machine',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='training',
            name='header',
        ),
        migrations.RemoveField(
            model_name='training',
            name='photo',
        ),
        migrations.AddField(
            model_name='itemforrent',
            name='header',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, verbose_name='Chapeau'),
        ),
        migrations.AlterField(
            model_name='card',
            name='link',
            field=models.URLField(blank=True, verbose_name='Lien'),
        ),
        migrations.AlterField(
            model_name='card',
            name='link_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='Text lien'),
        ),
        migrations.AddField(
            model_name='itemforrent',
            name='photo',
            field=models.ImageField(upload_to='img', verbose_name='Photo'),
        ),
        migrations.AddField(
            model_name='card',
            name='bootstrap_icon',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='card',
            name='icon',
            field=models.ImageField(blank=True, upload_to='icons', verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='card',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='icons', verbose_name='Icon'),
        ),
        migrations.AddField(
            model_name='itemforrent',
            name='background_color',
            field=colorfield.fields.ColorField(default='#0b1783', image_field=None, max_length=18, samples=[('#0b1783', 'blue'), ('#ddf9ff', 'blue-light'), ('#e3005c', 'red'), ('#ffe8e0', 'red-light'), ('#00a59f', 'green'), ('#e4f2e5', 'green-light')]),
        ),
        migrations.AddField(
            model_name='itemforrent',
            name='color',
            field=colorfield.fields.ColorField(default='#ffffff', image_field=None, max_length=18, samples=[('#0b1783', 'blue'), ('#ddf9ff', 'blue-light'), ('#e3005c', 'red'), ('#ffe8e0', 'red-light'), ('#00a59f', 'green'), ('#e4f2e5', 'green-light')]),
        ),
        migrations.AddField(
            model_name='itemforrent',
            name='desc',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='itemforrent',
            name='title',
            field=models.CharField(default='My title', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='machine',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='machines.machinecategory'),
        ),
        migrations.RemoveField(
            model_name='machine',
            name='spec',
        ),
        migrations.AlterModelOptions(
            name='card',
            options={'verbose_name': 'Carte', 'verbose_name_plural': 'Cartes'},
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name': 'FAQ', 'verbose_name_plural': 'FAQs'},
        ),
        migrations.AlterModelOptions(
            name='highlightmachine',
            options={'verbose_name': 'Atouts machine', 'verbose_name_plural': 'Atouts machine'},
        ),
        migrations.AlterModelOptions(
            name='machine',
            options={'verbose_name': 'Machine', 'verbose_name_plural': 'Machines'},
        ),
        migrations.AlterModelOptions(
            name='machinecategory',
            options={'verbose_name': 'Catégorie de machine', 'verbose_name_plural': 'Catégories de machine'},
        ),
        migrations.AlterModelOptions(
            name='machinegroup',
            options={'verbose_name': 'Groupe de machine', 'verbose_name_plural': 'Groupes de machine'},
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('value', djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                ('sort', models.PositiveSmallIntegerField(default=1)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machines.machine')),
            ],
            options={
                'verbose_name': 'Spécification',
                'verbose_name_plural': 'Spécifications',
            },
        ),
        migrations.AlterModelOptions(
            name='toolmachine',
            options={'verbose_name': 'Outil machine', 'verbose_name_plural': 'Outils machines'},
        ),
        migrations.AlterModelOptions(
            name='tooltraining',
            options={'verbose_name': 'Outil de formation', 'verbose_name_plural': 'Outils de formation'},
        ),
        migrations.AlterModelOptions(
            name='training',
            options={'verbose_name': 'Formation', 'verbose_name_plural': 'Formations'},
        ),
        migrations.AlterField(
            model_name='card',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='icons', verbose_name='Icone'),
        ),
    ]
