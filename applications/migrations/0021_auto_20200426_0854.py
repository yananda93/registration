# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-04-26 15:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applications', '0020_merge_20200426_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='blacklisted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blacklisted_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='application',
            name='reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('P', 'Under review'), ('R', 'Wait listed'), ('I', 'Invited'), ('LR', 'Last reminder'), ('C', 'Confirmed'), ('X', 'Cancelled'), ('A', 'Attended'), ('E', 'Expired'), ('D', 'Dubious'), ('IV', 'Invalid'), ('BL', 'Blacklisted')], default='P', max_length=2),
        ),
    ]
