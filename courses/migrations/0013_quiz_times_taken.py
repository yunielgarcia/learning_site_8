# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-06 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_course_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='times_taken',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]