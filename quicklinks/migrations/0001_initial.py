# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'QuickLinkGroup'
        db.create_table(u'quicklinks_quicklinkgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('order_int', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'quicklinks', ['QuickLinkGroup'])

        # Adding model 'QuickLink'
        db.create_table(u'quicklinks_quicklink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True)),
            ('quicklinkgroup', self.gf('django.db.models.fields.related.ForeignKey')(related_name='group', to=orm['quicklinks.QuickLinkGroup'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'quicklinks', ['QuickLink'])


    def backwards(self, orm):
        # Deleting model 'QuickLinkGroup'
        db.delete_table(u'quicklinks_quicklinkgroup')

        # Deleting model 'QuickLink'
        db.delete_table(u'quicklinks_quicklink')


    models = {
        u'quicklinks.quicklink': {
            'Meta': {'ordering': "['order']", 'object_name': 'QuickLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'quicklinkgroup': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'group'", 'to': u"orm['quicklinks.QuickLinkGroup']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'quicklinks.quicklinkgroup': {
            'Meta': {'ordering': "['order']", 'object_name': 'QuickLinkGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'order_int': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['quicklinks']