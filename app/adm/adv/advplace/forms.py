# -*- coding: utf-8 -*-

from django.forms import ModelForm
from app.models import AdvPlace


class Form(ModelForm):
    class Meta:
        model = AdvPlace