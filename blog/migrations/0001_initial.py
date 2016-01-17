# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields
import modelcluster.contrib.taggit
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('wagtailimages', '0005_make_filter_spec_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=250)),
                ('url', models.URLField()),
                ('imagen', models.ForeignKey(blank=True, to='wagtailimages.Image', related_name='+', null=True, on_delete=django.db.models.deletion.SET_NULL)),
            ],
            options={
                'verbose_name_plural': 'Anuncios',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, to='wagtailcore.Page', primary_key=True, auto_created=True, parent_link=True)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogIndexPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_external', models.URLField(verbose_name='Link Externo', blank=True)),
                ('title', models.CharField(help_text='Link title', max_length=255)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, to='wagtailcore.Page', primary_key=True, auto_created=True, parent_link=True)),
                ('resumen', wagtail.wagtailcore.fields.RichTextField()),
                ('body', wagtail.wagtailcore.fields.RichTextField()),
                ('extra_info', wagtail.wagtailcore.fields.RichTextField(default='')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('imagen', models.ForeignKey(blank=True, to='wagtailimages.Image', related_name='+', null=True, on_delete=django.db.models.deletion.SET_NULL)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_external', models.URLField(verbose_name='Link Externo', blank=True)),
                ('title', models.CharField(help_text='Link title', max_length=255)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogPageTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('content_object', modelcluster.fields.ParentalKey(to='blog.BlogPage', related_name='tagged_items')),
                ('tag', models.ForeignKey(to='taggit.Tag', related_name='blog_blogpagetag_items')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('label', models.CharField(help_text='The label of the form field', max_length=255)),
                ('field_type', models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time')], max_length=16)),
                ('required', models.BooleanField(default=True)),
                ('choices', models.CharField(help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.', blank=True, max_length=512)),
                ('default_value', models.CharField(help_text='Default value. Comma separated values supported for checkboxes.', blank=True, max_length=255)),
                ('help_text', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FormPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, to='wagtailcore.Page', primary_key=True, auto_created=True, parent_link=True)),
                ('to_address', models.CharField(help_text='Optional - form submissions will be emailed to this address', blank=True, max_length=255)),
                ('from_address', models.CharField(blank=True, max_length=255)),
                ('subject', models.CharField(blank=True, max_length=255)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('texto_agradecimiento', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='formfield',
            name='page',
            field=modelcluster.fields.ParentalKey(to='blog.FormPage', related_name='form_fields'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(blank=True, to='wagtailcore.Page', related_name='+', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(to='blog.BlogPage', related_name='related_links'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(verbose_name='Tags', help_text='A comma-separated list of tags.', blank=True, to='taggit.Tag', through='blog.BlogPageTag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogindexpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(blank=True, to='wagtailcore.Page', related_name='+', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogindexpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(to='blog.BlogIndexPage', related_name='related_links'),
            preserve_default=True,
        ),
    ]
