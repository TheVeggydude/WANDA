# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0005_auto_20151121_2237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='node',
            old_name='answer_text',
            new_name='answer',
        ),
    ]
