# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_follow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='following',
            new_name='user_from',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='follower',
            new_name='user_to',
        ),
    ]
