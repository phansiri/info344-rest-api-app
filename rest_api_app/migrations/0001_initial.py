# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=300)),
                ('publication_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('publisher', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('linkToBuy', models.CharField(max_length=300)),
                ('image', models.CharField(max_length=300)),
            ],
        ),
    ]
