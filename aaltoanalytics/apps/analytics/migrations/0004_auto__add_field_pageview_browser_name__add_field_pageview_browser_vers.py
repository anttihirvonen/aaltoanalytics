# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Pageview.browser_name'
        db.add_column('analytics_pageview', 'browser_name',
                      self.gf('django.db.models.fields.CharField')(default='Unknown', max_length=16),
                      keep_default=False)

        # Adding field 'Pageview.browser_version'
        db.add_column('analytics_pageview', 'browser_version',
                      self.gf('django.db.models.fields.CharField')(default='Unknown', max_length=16),
                      keep_default=False)

        # Adding field 'Pageview.operating_system'
        db.add_column('analytics_pageview', 'operating_system',
                      self.gf('django.db.models.fields.CharField')(default='Unknown', max_length=16),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Pageview.browser_name'
        db.delete_column('analytics_pageview', 'browser_name')

        # Deleting field 'Pageview.browser_version'
        db.delete_column('analytics_pageview', 'browser_version')

        # Deleting field 'Pageview.operating_system'
        db.delete_column('analytics_pageview', 'operating_system')

    models = {
        'analytics.pageview': {
            'Meta': {'object_name': 'Pageview'},
            'browser_name': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'browser_version': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_read_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'operating_system': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'referrer': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'screen_height': ('django.db.models.fields.IntegerField', [], {}),
            'screen_width': ('django.db.models.fields.IntegerField', [], {}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['analytics.Service']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total_read_time': ('django.db.models.fields.IntegerField', [], {}),
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