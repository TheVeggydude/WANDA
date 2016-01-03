# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0002_auto_20151121_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='answer_text',
            field=models.CharField(max_length=400, default='answer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='node',
            name='question_text',
            field=models.CharField(max_length=200, default='question'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='node',
            name='result',
            field=models.BooleanField(default=False),
        ),
    ]
