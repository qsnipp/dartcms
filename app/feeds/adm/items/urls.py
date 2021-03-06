# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'


from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _

from lib.views.adm.generic import DataGridView, GridView, InsertObjectView, UpdateObjectView, DeleteObjectView
from app.feeds.models import FeedItem as Model
from forms import Form

grid_columns = (
    ('name', _(u"Name"), 'string', '40%'),
    ('date_published', _(u"Date of Publication"), 'datetime', '40%'),
    ('is_visible', _(u"Show on Site"), 'boolean', '20%'),
)

search_by = (
    ('name', _(u"Name"), 'string'),
    ('date_published', _(u"Date of Publication"), 'datetime'),
    ('is_visible', _(u"Show on Site"), 'boolean'),
)

kwargs = {
    'grid_columns': grid_columns,
    'search_by': search_by,
    'model': Model,
    'form_class': Form,
    'parent_kwarg_name': 'feed',
    'parent_model_fk': 'feed_id'
}

grid_kwargs = kwargs.copy()
grid_kwargs.update({
    'paginate_by': 1
})

urlpatterns = patterns('',
    url(r'^$', login_required(GridView.as_view(**grid_kwargs)), name='index'),
    url(r'^page/(?P<page>\d+)/$', login_required(GridView.as_view(**grid_kwargs)), name='index'),
    url(r'^insert/$', login_required(InsertObjectView.as_view(**kwargs)), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', login_required(UpdateObjectView.as_view(**kwargs)), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(DeleteObjectView.as_view(**kwargs)), name='delete'),
)