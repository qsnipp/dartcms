# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-24 06:02
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dartcms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Shows inside the title tag', max_length=255, verbose_name='Title')),
                ('header', models.CharField(max_length=255, verbose_name='Page Header')),
                ('menu_name', models.CharField(default=b'', max_length=255, verbose_name='Menu name')),
                ('menu_url', models.CharField(blank=True, default=b'', max_length=255, verbose_name='URL for Redirect')),
                ('slug', models.SlugField(default=b'', verbose_name='URL')),
                ('url', models.CharField(max_length=512)),
                ('sort', models.IntegerField(default=1)),
                ('module_params', models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='Module parameters')),
                ('before_content', models.TextField(blank=True, default=b'', verbose_name='Before Content')),
                ('after_content', models.TextField(blank=True, default=b'', verbose_name='After Content')),
                ('seo_keywords', models.TextField(blank=True, default=b'', verbose_name='Keywords (meta keywords)')),
                ('seo_description', models.TextField(blank=True, default=b'', verbose_name='Description (meta description)')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Is Enabled')),
                ('is_in_menu', models.BooleanField(default=True, verbose_name='Show in Menu')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('adv_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dartcms.AdvSection', verbose_name='Ads')),
            ],
            options={
                'ordering': ['sort'],
                'abstract': False,
                'verbose_name': 'page',
                'verbose_name_plural': 'pages',
            },
        ),
        migrations.CreateModel(
            name='PageModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=64, verbose_name='Name (RU)')),
                ('name_en', models.CharField(max_length=64, verbose_name='Name (EN)')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Is Enabled')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Module',
                'verbose_name_plural': 'Modules',
            },
        ),
        migrations.AddField(
            model_name='page',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.PageModule', verbose_name='Module'),
        ),
        migrations.AddField(
            model_name='page',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='pages.Page', verbose_name='Parent Page'),
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([('module', 'slug')]),
        ),
    ]
