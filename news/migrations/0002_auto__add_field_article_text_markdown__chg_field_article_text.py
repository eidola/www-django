# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.text_markdown'
        db.add_column('news_article', 'text_markdown',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)


        # Changing field 'Article.text'
        db.alter_column('news_article', 'text', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):
        # Deleting field 'Article.text_markdown'
        db.delete_column('news_article', 'text_markdown')


        # Changing field 'Article.text'
        db.alter_column('news_article', 'text', self.gf('django.db.models.fields.TextField')(default='blank'))

    models = {
        'news.article': {
            'Meta': {'object_name': 'Article'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'text_markdown': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['news']