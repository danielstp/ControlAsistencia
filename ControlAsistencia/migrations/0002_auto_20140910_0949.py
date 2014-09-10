# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ControlAsistencia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beca',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nombre',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nombre', models.CharField(verbose_name='Nombre', max_length=50, blank=True)),
                ('apellido', models.CharField(verbose_name='1er Apellido', max_length=20, blank=True)),
                ('apellido2', models.CharField(verbose_name='2do Apellido ', max_length=20, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='estudiante',
            old_name='apellido',
            new_name='telefono',
        ),
        migrations.AddField(
            model_name='centro',
            name='codigo',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='centro',
            name='direccion',
            field=models.ForeignKey(default=1, to='ControlAsistencia.Direccion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='centro',
            name='email',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='centro',
            name='expediente',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='centro',
            name='fax',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='centro',
            name='personal',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='centro',
            name='telefono',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estudiante',
            name='telefonoAlt',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutor',
            name='direccion',
            field=models.ForeignKey(default=1, to='ControlAsistencia.Direccion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutor',
            name='dni',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutor',
            name='email',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutor',
            name='telefono',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutor',
            name='telefonoAlt',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='nombre',
            field=models.ForeignKey(to='ControlAsistencia.Nombre'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='nombre',
            field=models.ForeignKey(to='ControlAsistencia.Nombre'),
        ),
    ]
