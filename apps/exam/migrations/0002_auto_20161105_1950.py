# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 19:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Added_wish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.User')),
                ('wish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Wish')),
            ],
        ),
        migrations.RemoveField(
            model_name='member',
            name='joiner',
        ),
        migrations.RemoveField(
            model_name='member',
            name='trip',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]