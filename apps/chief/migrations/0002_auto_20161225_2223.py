# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-25 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chief', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=512, verbose_name='Название'),
        ),
    ]