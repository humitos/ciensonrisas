# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Message.last_name'
        db.delete_column('website_message', 'last_name')

        # Deleting field 'Message.first_name'
        db.delete_column('website_message', 'first_name')

        # Deleting field 'Message.nickname'
        db.delete_column('website_message', 'nickname')

        # Adding field 'Message.name'
        db.add_column('website_message', 'name',
                      self.gf('django.db.models.fields.CharField')(default='No name', max_length=30),
                      keep_default=False)

        # Adding field 'Message.subject'
        db.add_column('website_message', 'subject',
                      self.gf('django.db.models.fields.CharField')(default='No subject', max_length=100),
                      keep_default=False)


        # Changing field 'Message.url'
        db.alter_column('website_message', 'url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

    def backwards(self, orm):
        # Adding field 'Message.last_name'
        db.add_column('website_message', 'last_name',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Message.first_name'
        db.add_column('website_message', 'first_name',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Message.nickname'
        db.add_column('website_message', 'nickname',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Message.name'
        db.delete_column('website_message', 'name')

        # Deleting field 'Message.subject'
        db.delete_column('website_message', 'subject')


        # Changing field 'Message.url'
        db.alter_column('website_message', 'url', self.gf('django.db.models.fields.URLField')(default='http://example.com', max_length=200))

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
        'website.message': {
            'Meta': {'object_name': 'Message'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
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
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Place']"})
        }
    }

    complete_apps = ['website']