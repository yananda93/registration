# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-05-07 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_user_types_20200321_0441'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='can_review_mentors',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='can_review_sponsors',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='can_review_volunteers',
            field=models.BooleanField(default=False),
        ),
    ]