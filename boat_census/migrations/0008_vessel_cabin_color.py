# Generated by Django 2.2.4 on 2019-08-22 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boat_census', '0007_remove_vessel_cabin_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='vessel',
            name='cabin_color',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
