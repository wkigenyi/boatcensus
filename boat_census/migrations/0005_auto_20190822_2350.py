# Generated by Django 2.2.4 on 2019-08-22 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boat_census', '0004_vessel_cabin_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vessel',
            name='hull_color',
        ),
        migrations.AddField(
            model_name='vessel',
            name='hull_color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boat_census.Color'),
        ),
    ]
