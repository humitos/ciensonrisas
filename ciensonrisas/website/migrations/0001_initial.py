# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Place'
        db.create_table('website_place', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('website', ['Place'])

        # Adding model 'Smile'
        db.create_table('website_smile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Place'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Author'])),
        ))
        db.send_create_signal('website', ['Smile'])

        # Adding model 'Author'
        db.create_table('website_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('sign', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('website', ['Author'])


    def backwards(self, orm):
        # Deleting model 'Place'
        db.delete_table('website_place')

        # Deleting model 'Smile'
        db.delete_table('website_smile')

        # Deleting model 'Author'
        db.delete_table('website_author')


    models = {
        'website.author': {
            'Meta': {'object_name': 'Author'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'sign': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'website.place': {
            'Meta': {'object_name': 'Place'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'website.smile': {
            'Meta': {'object_name': 'Smile'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Author']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Place']"})
        }
    }

    complete_apps = ['website']