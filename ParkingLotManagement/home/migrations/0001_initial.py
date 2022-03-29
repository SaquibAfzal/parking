# Generated by Django 4.0.3 on 2022-03-26 10:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='searching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownername', models.CharField(max_length=122)),
                ('vtype', models.CharField(max_length=122)),
                ('vno', models.CharField(max_length=122, unique='true')),
                ('row_no', models.SmallIntegerField()),
                ('pos_no', models.SmallIntegerField()),
                ('occupancy', models.SmallIntegerField()),
                ('intime', models.TimeField(verbose_name=datetime.time)),
            ],
        ),
    ]
