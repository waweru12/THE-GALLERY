# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-16 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appgallery', '0003_auto_20190616_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='appgallery/'),
        ),
    ]
