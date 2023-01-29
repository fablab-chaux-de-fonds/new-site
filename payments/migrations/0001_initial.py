# Generated by Django 3.2.16 on 2023-01-29 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('accounts', '0004_merge_0003_auto_20220320_2116_0003_auto_20221222_0802'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutButtonPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='payments_checkoutbuttonpluginmodel', serialize=False, to='cms.cmsplugin')),
                ('text', models.CharField(default=None, max_length=64, null=True)),
                ('subscription_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.subscriptioncategory')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
