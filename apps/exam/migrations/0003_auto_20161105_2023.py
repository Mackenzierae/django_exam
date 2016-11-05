# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 20:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20161105_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Added',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Wish')),
                ('wish_adder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='added_wish',
            name='adder',
        ),
        migrations.RemoveField(
            model_name='added_wish',
            name='wish',
        ),
        migrations.DeleteModel(
            name='Added_wish',
        ),
    ]