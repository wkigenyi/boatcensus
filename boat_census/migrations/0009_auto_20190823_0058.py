# Generated by Django 2.2.4 on 2019-08-22 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boat_census', '0008_vessel_cabin_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vessel',
            name='cabin_color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cabincolor', to='boat_census.Color'),
        ),
    ]
