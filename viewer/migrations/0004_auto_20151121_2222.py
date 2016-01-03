# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0003_auto_20151121_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='answer_text',
            field=models.CharField(default='answer', max_length=400),
        ),
        migrations.AlterField(
            model_name='node',
            name='question_text',
            field=models.CharField(default='question', max_length=200),
        ),
    ]
