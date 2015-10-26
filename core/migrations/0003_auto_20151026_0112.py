# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151026_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email_Address',
            field=models.TextField(default=b'', max_length=300),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_Name',
            field=models.TextField(default=b'', max_length=300),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_Name',
            field=models.TextField(default=b'', max_length=300),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(default=b'', max_length=300),
        ),
    ]
