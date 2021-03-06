# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

import datetime

from django import forms
from django.utils.translation import ugettext_lazy as _

from app.feeds.models import FeedItem


class Form(forms.ModelForm):
    class Meta:
        model = FeedItem
        exclude = ['feed', 'slug']
        widgets = {
            'short_text': forms.Textarea(attrs={'class': 'rte'}),
            'full_text': forms.Textarea(attrs={'class': 'rte'}),
        }

    date_published = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'class': 'datetime'
            }
        ),
        input_formats=["%d.%m.%Y %H:%M:%S", "%Y-%m-%d %H:%M:%S"],
        initial=datetime.datetime.now,
        label=_(u'Date of publication')
    )