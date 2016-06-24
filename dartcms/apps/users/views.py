# -*- coding: utf-8 -*-
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView

from dartcms.views import AdminMixin, InsertObjectView, UpdateObjectView


class ChangePasswordView(AdminMixin, FormView):
    form_class = AdminPasswordChangeForm
    page_header = _(u'Users')
    template_name = 'dartcms/apps/users/change_password.html'
    success_url = 'users:index'

    def get_form_kwargs(self):
        kwargs = super(ChangePasswordView, self).get_form_kwargs()
        kwargs.update({
            'user': User.objects.get(pk=self.kwargs['pk'])
        })
        return kwargs


class CMSUserUpdateView(UpdateObjectView):
    success_url = 'users:index'

    def get_initial(self):
        obj = self.get_object()
        return {'modules': obj.module_set.all()}


class CMSUserInsertView(InsertObjectView):
    success_url = 'users:change_password'