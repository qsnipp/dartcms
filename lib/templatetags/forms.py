__author__ = 'Dmitry Astrikov'

from django import template
from django.forms import CheckboxInput, HiddenInput, ClearableFileInput, RadioSelect, SelectMultiple

from lib.forms import ClearableMultiFileInput

register = template.Library()


@register.filter(name='is_checkbox')
def is_checkbox(field):
    return field.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__


@register.filter(name='is_hidden')
def is_hidden(field):
    return field.field.widget.__class__.__name__ == HiddenInput().__class__.__name__


@register.filter(name='is_file')
def is_file(field):
    return field.field.widget.__class__.__name__ == ClearableFileInput().__class__.__name__


@register.filter(name='is_radio')
def is_radio(field):
    return field.field.widget.__class__.__name__ == RadioSelect().__class__.__name__


@register.filter(name='is_multiple_select')
def is_multiple_select(field):
    return field.field.widget.__class__.__name__ == SelectMultiple().__class__.__name__


@register.filter(name='is_multiple_file')
def is_multiple_file(field):
    return field.field.widget.__class__.__name__ == ClearableMultiFileInput().__class__.__name__


@register.filter(name='test_widget_class')
def test_widget_class(field):
    return field.field.widget.__class__.__name__
