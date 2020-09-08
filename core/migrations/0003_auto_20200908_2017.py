# Generated by Django 3.1.1 on 2020-09-08 20:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_usertask'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='site_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='car_reg',
            field=models.CharField(blank=True, choices=[('SM16 SWF', 'SM16 SWF - Richards (White Toyota Hilux)'), ('FL64 EBN', 'FL64 EBN - Scotts (White Toyota Hilux)'), ('WG63 LVZ', 'WG63 LVZ - Volkswagen Caddy Van'), ('SC16 SYZ', 'SC16 SYZ - Vauxhall Movano Flatbed Truck'), ('SA13 KLJ', 'SA13 KLJ - Daniels (White Ford Ranger'), ('SJ62 RMU', 'SJ62 RMU - Matts (Black Toyota Hilux'), ('HG61 HGZ', 'HG61 HGZ - Tims (Blue Toyota Hilux)'), ('XXX', 'XXX - Alexs (Grey Toyota Hilux)')], max_length=20, null=True),
        ),
    ]