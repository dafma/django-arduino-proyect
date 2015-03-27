# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil_Usuarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=255)),
                ('Apellido', models.CharField(max_length=255)),
                ('Direccion', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'perfil_usuarios',
            },
            bases=(models.Model,),
        ),
    ]
