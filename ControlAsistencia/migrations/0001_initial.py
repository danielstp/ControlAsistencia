# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Provincia'
        db.create_table(u'ControlAsistencia_provincia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'ControlAsistencia', ['Provincia'])

        # Adding model 'ComunidadAutonoma'
        db.create_table(u'ControlAsistencia_comunidadautonoma', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'ControlAsistencia', ['ComunidadAutonoma'])

        # Adding model 'Direccion'
        db.create_table(u'ControlAsistencia_direccion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('departamento', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('edificio', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('piso', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('casa', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('calle1', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('calle2', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('codigoPostal', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('ciudad', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('provincia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.Provincia'])),
            ('comunidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.ComunidadAutonoma'])),
            ('pais', self.gf('django_countries.fields.CountryField')(max_length=2)),
        ))
        db.send_create_signal(u'ControlAsistencia', ['Direccion'])

        # Adding model 'Telefono'
        db.create_table(u'ControlAsistencia_telefono', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=0)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=12)),
        ))
        db.send_create_signal(u'ControlAsistencia', ['Telefono'])

        # Adding model 'Persona'
        db.create_table(u'ControlAsistencia_persona', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('apellido2', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('direccion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.Direccion'])),
            ('dni', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('telefono', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.Telefono'])),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('nacionalidad', self.gf('django_countries.fields.CountryField')(max_length=2)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'ControlAsistencia', ['Persona'])

        # Adding model 'Contacto'
        db.create_table(u'ControlAsistencia_contacto', (
            (u'persona_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ControlAsistencia.Persona'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'ControlAsistencia', ['Contacto'])

        # Adding model 'EstudianteBase'
        db.create_table(u'ControlAsistencia_estudiantebase', (
            (u'persona_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ControlAsistencia.Persona'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'ControlAsistencia', ['EstudianteBase'])

        # Adding model 'TipoMenu'
        db.create_table(u'ControlAsistencia_tipomenu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'ControlAsistencia', ['TipoMenu'])

        # Adding model 'Menu'
        db.create_table(u'ControlAsistencia_menu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('costo', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.TipoMenu'])),
        ))
        db.send_create_signal(u'ControlAsistencia', ['Menu'])

        # Adding model 'Banco'
        db.create_table(u'ControlAsistencia_banco', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('iban', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('codigoOficina', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('dc1', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('dc2', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('bic', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('fp', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('telefono', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.Telefono'])),
        ))
        db.send_create_signal(u'ControlAsistencia', ['Banco'])

        # Adding model 'CuentaBanco'
        db.create_table(u'ControlAsistencia_cuentabanco', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('banco', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.Banco'])),
        ))
        db.send_create_signal(u'ControlAsistencia', ['CuentaBanco'])

        # Adding model 'Beca'
        db.create_table(u'ControlAsistencia_beca', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('monto', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
        ))
        db.send_create_signal(u'ControlAsistencia', ['Beca'])

        # Adding model 'Centro'
        db.create_table(u'ControlAsistencia_centro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('direccion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.Direccion'])),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lote', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('expediente', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('director', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Director', to=orm['ControlAsistencia.Contacto'])),
            ('responsable', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Responsable', to=orm['ControlAsistencia.Contacto'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('encargado', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Encargado', to=orm['ControlAsistencia.Contacto'])),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('precioComida', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('precioDesayuno', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('montoBeca', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('telefono', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.Telefono'])),
        ))
        db.send_create_signal(u'ControlAsistencia', ['Centro'])

        # Adding M2M table for field beca on 'Centro'
        m2m_table_name = db.shorten_name(u'ControlAsistencia_centro_beca')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('centro', models.ForeignKey(orm[u'ControlAsistencia.centro'], null=False)),
            ('beca', models.ForeignKey(orm[u'ControlAsistencia.beca'], null=False))
        ))
        db.create_unique(m2m_table_name, ['centro_id', 'beca_id'])

        # Adding model 'Tutor'
        db.create_table(u'ControlAsistencia_tutor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('persona', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ControlAsistencia.Persona'], unique=True)),
            ('cuenta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.CuentaBanco'])),
        ))
        db.send_create_signal(u'ControlAsistencia', ['Tutor'])

        # Adding model 'Pagador'
        db.create_table(u'ControlAsistencia_pagador', (
            (u'persona_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ControlAsistencia.Persona'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'ControlAsistencia', ['Pagador'])

        # Adding model 'Etapa'
        db.create_table(u'ControlAsistencia_etapa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'ControlAsistencia', ['Etapa'])

        # Adding model 'Curso'
        db.create_table(u'ControlAsistencia_curso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('etapa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.Etapa'])),
            ('nivel', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'ControlAsistencia', ['Curso'])

        # Adding model 'Estudiante'
        db.create_table(u'ControlAsistencia_estudiante', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.Persona'])),
            ('curso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.Curso'])),
            ('dieta', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('nutricion', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('tutor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.Tutor'])),
            ('pagador', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pagador', to=orm['ControlAsistencia.Pagador'])),
            ('centro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.Centro'])),
            ('nacimiento', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'ControlAsistencia', ['Estudiante'])

        # Adding model 'Documento'
        db.create_table(u'ControlAsistencia_documento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('archivo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.Estudiante'])),
        ))
        db.send_create_signal(u'ControlAsistencia', ['Documento'])

        # Adding model 'Pago'
        db.create_table(u'ControlAsistencia_pago', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fechaHora', self.gf('django.db.models.fields.DateTimeField')()),
            ('monto', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('tutor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.Pagador'])),
            ('estudiante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.Estudiante'])),
            ('formaPago', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
        ))
        db.send_create_signal(u'ControlAsistencia', ['Pago'])

        # Adding model 'Asistencia'
        db.create_table(u'ControlAsistencia_asistencia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('asistente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.Estudiante'])),
            ('fechaHora', self.gf('django.db.models.fields.DateTimeField')()),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.Menu'])),
        ))
        db.send_create_signal(u'ControlAsistencia', ['Asistencia'])

        # Adding model 'Becado'
        db.create_table(u'ControlAsistencia_becado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estudiante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.Estudiante'])),
            ('beca', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.Beca'])),
            ('monto', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('final', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'ControlAsistencia', ['Becado'])

        # Adding model 'BecaCentro'
        db.create_table(u'ControlAsistencia_becacentro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('centro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.Centro'])),
            ('beca', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.Beca'])),
            ('monto', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
        ))
        db.send_create_signal(u'ControlAsistencia', ['BecaCentro'])

        # Adding model 'PlanAsistencia'
        db.create_table(u'ControlAsistencia_planasistencia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estudiante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ControlAsistencia.Estudiante'])),
            ('lunes', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('martes', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('miercoles', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('jueves', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('viernes', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sabado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('domingo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fechaInicio', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'ControlAsistencia', ['PlanAsistencia'])


    def backwards(self, orm):
        # Deleting model 'Provincia'
        db.delete_table(u'ControlAsistencia_provincia')

        # Deleting model 'ComunidadAutonoma'
        db.delete_table(u'ControlAsistencia_comunidadautonoma')

        # Deleting model 'Direccion'
        db.delete_table(u'ControlAsistencia_direccion')

        # Deleting model 'Telefono'
        db.delete_table(u'ControlAsistencia_telefono')

        # Deleting model 'Persona'
        db.delete_table(u'ControlAsistencia_persona')

        # Deleting model 'Contacto'
        db.delete_table(u'ControlAsistencia_contacto')

        # Deleting model 'EstudianteBase'
        db.delete_table(u'ControlAsistencia_estudiantebase')

        # Deleting model 'TipoMenu'
        db.delete_table(u'ControlAsistencia_tipomenu')

        # Deleting model 'Menu'
        db.delete_table(u'ControlAsistencia_menu')

        # Deleting model 'Banco'
        db.delete_table(u'ControlAsistencia_banco')

        # Deleting model 'CuentaBanco'
        db.delete_table(u'ControlAsistencia_cuentabanco')

        # Deleting model 'Beca'
        db.delete_table(u'ControlAsistencia_beca')

        # Deleting model 'Centro'
        db.delete_table(u'ControlAsistencia_centro')

        # Removing M2M table for field beca on 'Centro'
        db.delete_table(db.shorten_name(u'ControlAsistencia_centro_beca'))

        # Deleting model 'Tutor'
        db.delete_table(u'ControlAsistencia_tutor')

        # Deleting model 'Pagador'
        db.delete_table(u'ControlAsistencia_pagador')

        # Deleting model 'Etapa'
        db.delete_table(u'ControlAsistencia_etapa')

        # Deleting model 'Curso'
        db.delete_table(u'ControlAsistencia_curso')

        # Deleting model 'Estudiante'
        db.delete_table(u'ControlAsistencia_estudiante')

        # Deleting model 'Documento'
        db.delete_table(u'ControlAsistencia_documento')

        # Deleting model 'Pago'
        db.delete_table(u'ControlAsistencia_pago')

        # Deleting model 'Asistencia'
        db.delete_table(u'ControlAsistencia_asistencia')

        # Deleting model 'Becado'
        db.delete_table(u'ControlAsistencia_becado')

        # Deleting model 'BecaCentro'
        db.delete_table(u'ControlAsistencia_becacentro')

        # Deleting model 'PlanAsistencia'
        db.delete_table(u'ControlAsistencia_planasistencia')


    models = {
        u'ControlAsistencia.asistencia': {
            'Meta': {'object_name': 'Asistencia'},
            'asistente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.Estudiante']"}),
            'fechaHora': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.Menu']"})
        },
        u'ControlAsistencia.banco': {
            'Meta': {'object_name': 'Banco'},
            'bic': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'codigoOficina': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'dc1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'dc2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'fp': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'iban': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'telefono': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.Telefono']"})
        },
        u'ControlAsistencia.beca': {
            'Meta': {'object_name': 'Beca'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'ControlAsistencia.becacentro': {
            'Meta': {'object_name': 'BecaCentro'},
            'beca': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.Beca']"}),
            'centro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.Centro']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'})
        },
        u'ControlAsistencia.becado': {
            'Meta': {'object_name': 'Becado'},
            'beca': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.Beca']"}),
            'estudiante': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.Estudiante']"}),
            'final': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'})
        },
        u'ControlAsistencia.centro': {
            'Meta': {'object_name': 'Centro'},
            'beca': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['ControlAsistencia.Beca']", 'null': 'True', 'blank': 'True'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'direccion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.Direccion']"}),
            'director': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Director'", 'to': u"orm['ControlAsistencia.Contacto']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'encargado': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Encargado'", 'to': u"orm['ControlAsistencia.Contacto']"}),
            'expediente': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lote': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'montoBeca': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'precioComida': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'precioDesayuno': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'responsable': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Responsable'", 'to': u"orm['ControlAsistencia.Contacto']"}),
            'telefono': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.Telefono']"})
        },
        u'ControlAsistencia.comunidadautonoma': {
            'Meta': {'object_name': 'ComunidadAutonoma'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'ControlAsistencia.contacto': {
            'Meta': {'object_name': 'Contacto', '_ormbases': [u'ControlAsistencia.Persona']},
            u'persona_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ControlAsistencia.Persona']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'ControlAsistencia.cuentabanco': {
            'Meta': {'object_name': 'CuentaBanco'},
            'banco': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.Banco']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'ControlAsistencia.curso': {
            'Meta': {'object_name': 'Curso'},
            'etapa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.Etapa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'ControlAsistencia.direccion': {
            'Meta': {'object_name': 'Direccion'},
            'calle1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'calle2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'casa': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'codigoPostal': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'comunidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.ComunidadAutonoma']"}),
            'departamento': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'edificio': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'pais': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'piso': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'provincia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.Provincia']"})
        },
        u'ControlAsistencia.documento': {
            'Meta': {'object_name': 'Documento'},
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.Estudiante']"})
        },
        u'ControlAsistencia.estudiante': {
            'Meta': {'object_name': 'Estudiante'},
            'centro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.Centro']"}),
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.Curso']"}),
            'dieta': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nacimiento': ('django.db.models.fields.DateField', [], {}),
            'nutricion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'pagador': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pagador'", 'to': u"orm['ControlAsistencia.Pagador']"}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.Persona']"}),
            'tutor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.Tutor']"})
        },
        u'ControlAsistencia.estudiantebase': {
            'Meta': {'object_name': 'EstudianteBase', '_ormbases': [u'ControlAsistencia.Persona']},
            u'persona_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ControlAsistencia.Persona']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'ControlAsistencia.etapa': {
            'Meta': {'object_name': 'Etapa'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'ControlAsistencia.menu': {
            'Meta': {'object_name': 'Menu'},
            'costo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.TipoMenu']"})
        },
        u'ControlAsistencia.pagador': {
            'Meta': {'object_name': 'Pagador', '_ormbases': [u'ControlAsistencia.Persona']},
            u'persona_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ControlAsistencia.Persona']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'ControlAsistencia.pago': {
            'Meta': {'object_name': 'Pago'},
            'estudiante': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.Estudiante']"}),
            'fechaHora': ('django.db.models.fields.DateTimeField', [], {}),
            'formaPago': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'tutor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.Pagador']"})
        },
        u'ControlAsistencia.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'apellido2': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.Direccion']"}),
            'dni': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nacionalidad': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.Telefono']"})
        },
        u'ControlAsistencia.planasistencia': {
            'Meta': {'object_name': 'PlanAsistencia'},
            'domingo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'estudiante': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.Estudiante']"}),
            'fechaInicio': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jueves': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lunes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'martes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'miercoles': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sabado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'viernes': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'ControlAsistencia.provincia': {
            'Meta': {'object_name': 'Provincia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'ControlAsistencia.telefono': {
            'Meta': {'object_name': 'Telefono'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '0'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'ControlAsistencia.tipomenu': {
            'Meta': {'object_name': 'TipoMenu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'ControlAsistencia.tutor': {
            'Meta': {'object_name': 'Tutor'},
            'cuenta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ControlAsistencia.CuentaBanco']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ControlAsistencia.Persona']", 'unique': 'True'})
        }
    }

    complete_apps = ['ControlAsistencia']