# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_remove_user_following'),
        ('account', '0004_contact'),
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
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
