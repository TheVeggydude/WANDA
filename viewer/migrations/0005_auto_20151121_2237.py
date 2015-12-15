# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0004_auto_20151121_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('text', models.CharField(max_length=400, default='answer')),
            ],
        ),
        migrations.AlterField(
            model_name='node',
            name='answer_text',
            field=models.ForeignKey(to='viewer.Answer'),
        ),
    ]
