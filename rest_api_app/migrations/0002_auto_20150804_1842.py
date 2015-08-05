# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.URLField(max_length=400),
        ),
        migrations.AlterField(
            model_name='books',
            name='linkToBuy',
            field=models.URLField(max_length=400),
        ),
    ]
