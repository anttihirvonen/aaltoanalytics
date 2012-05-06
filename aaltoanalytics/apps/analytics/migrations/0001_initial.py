# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Service'
        db.create_table('analytics_service', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('tracking_id', self.gf('django.db.models.fields.CharField')(max_length=8)),
        ))
        db.send_create_signal('analytics', ['Service'])

        # Adding model 'Pageview'
        db.create_table('analytics_pageview', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analytics.Service'])),
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('screen_width', self.gf('django.db.models.fields.IntegerField')()),
            ('screen_height', self.gf('django.db.models.fields.IntegerField')()),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('referrer', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('analytics', ['Pageview'])

    def backwards(self, orm):
        # Deleting model 'Service'
        db.delete_table('analytics_service')

        # Deleting model 'Pageview'
        db.delete_table('analytics_pageview')

    models = {
        'analytics.pageview': {
            'Meta': {'object_name': 'Pageview'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'referrer': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'screen_height': ('django.db.models.fields.IntegerField', [], {}),
            'screen_width': ('django.db.models.fields.IntegerField', [], {}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['analytics.Service']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'analytics.service': {
            'Meta': {'object_name': 'Service'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'tracking_id': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        }
    }

    complete_apps = ['analytics']