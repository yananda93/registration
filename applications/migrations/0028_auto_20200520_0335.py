# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-05-20 10:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0027_auto_20200519_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsorapplication',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sponsorapplication',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsorapplication_application', to=settings.AUTH_USER_MODEL),
        ),
    ]