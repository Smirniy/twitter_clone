# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user_from',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user_to',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='date_of_birth',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
