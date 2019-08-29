# Generated by Django 2.2.4 on 2019-08-29 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boat_census', '0009_auto_20190823_0058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='color',
            old_name='color',
            new_name='color_name',
        ),
        migrations.AddField(
            model_name='color',
            name='color_code',
            field=models.CharField(default=1, max_length=7),
            preserve_default=False,
        ),
    ]
