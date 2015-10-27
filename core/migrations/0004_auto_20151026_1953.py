# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151026_0112'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='title',
            field=models.IntegerField(default=0, choices=[(0, b'Dr.'), (1, b'Mr.'), (2, b'Mrs.'), (3, b'Miss')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email_Address',
            field=models.CharField(default=b'', max_length=300),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_Name',
            field=models.CharField(default=b'', max_length=300),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_Name',
            field=models.CharField(default=b'', max_length=300),
        ),
    ]
