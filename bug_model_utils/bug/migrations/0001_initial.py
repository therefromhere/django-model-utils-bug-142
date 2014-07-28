# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', model_utils.fields.StatusField(default=b'NEW', max_length=100, no_check_for_status=True, choices=[(b'', b''), (b'NEW', b'NEW'), (b'INACTIVE', b'INACTIVE'), (b'ACTIVE', b'ACTIVE')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
