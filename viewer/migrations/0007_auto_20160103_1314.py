# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-03 13:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0006_auto_20151121_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='Please update this question text.', max_length=400)),
                ('children', models.ManyToManyField(blank=True, null=True, related_name='parents', to='viewer.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewer.Question')),
            ],
        ),
        migrations.RemoveField(
            model_name='node',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='node',
            name='parent',
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.CharField(default='Please update this answer text.', max_length=400),
        ),
        migrations.DeleteModel(
            name='Node',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='viewer.Question'),
        ),
    ]
