# Generated by Django 4.0.3 on 2022-03-26 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='searching',
            old_name='intime',
            new_name='in_time',
        ),
        migrations.RenameField(
            model_name='searching',
            old_name='ownername',
            new_name='owner_name',
        ),
        migrations.RenameField(
            model_name='searching',
            old_name='vno',
            new_name='vehicle_no',
        ),
        migrations.RenameField(
            model_name='searching',
            old_name='vtype',
            new_name='vehicle_type',
        ),
    ]
