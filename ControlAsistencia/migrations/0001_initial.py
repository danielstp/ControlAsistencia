# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asistio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('fechaHora', models.DateTimeField(verbose_name='Fecha y hora de la asistencia')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Centro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('type', models.CharField(verbose_name='Type', max_length=20, choices=[('CASA', 'Casa')])),
                ('departamento', models.CharField(verbose_name='Departement', blank=True, max_length=50)),
                ('edificio', models.CharField(verbose_name='Building', blank=True, max_length=20)),
                ('piso', models.CharField(verbose_name='Floor', blank=True, max_length=20)),
                ('casa', models.CharField(verbose_name='Door', blank=True, max_length=20)),
                ('numero', models.CharField(verbose_name='Number', blank=True, max_length=30)),
                ('calle1', models.CharField(verbose_name='Address 1', blank=True, max_length=100)),
                ('calle2', models.CharField(verbose_name='Address 2', blank=True, max_length=100)),
                ('codigoPostal', models.CharField(verbose_name='ZIP code', blank=True, max_length=5)),
                ('localidad', models.CharField(verbose_name='City', blank=True, max_length=100)),
                ('provincia', models.CharField(verbose_name='State', blank=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('dni', models.CharField(max_length=255)),
                ('curso', models.CharField(max_length=255)),
                ('dieta', models.CharField(max_length=255)),
                ('nutricion', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('etapa', models.CharField(max_length=255)),
                ('desayuno', models.BooleanField(default=True)),
                ('comida', models.BooleanField(default=True)),
                ('descuento', models.DecimalField(max_digits=12, decimal_places=2)),
                ('centro', models.ForeignKey(to='ControlAsistencia.Centro')),
                ('direccion', models.ForeignKey(to='ControlAsistencia.Direccion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('costo', models.DecimalField(max_digits=12, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('fechaHora', models.DateTimeField(verbose_name='Fecha y hora del pago')),
                ('monto', models.DecimalField(max_digits=12, decimal_places=2)),
                ('estudiante', models.ForeignKey(to='ControlAsistencia.Estudiante')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pago',
            name='tutor',
            field=models.ForeignKey(to='ControlAsistencia.Tutor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiante',
            name='tutor',
            field=models.ForeignKey(to='ControlAsistencia.Tutor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asistio',
            name='asistente',
            field=models.ForeignKey(to='ControlAsistencia.Estudiante'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asistio',
            name='menu',
            field=models.ForeignKey(to='ControlAsistencia.Menu'),
            preserve_default=True,
        ),
    ]
