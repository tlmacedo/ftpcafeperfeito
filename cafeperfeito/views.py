# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView

from cafeperfeito.forms import LoginForm
from cafeperfeito.models import Usuario


class LoginTemplateView(FormView):
    # model = Usuario
    form_class = LoginForm
    template_name = 'cafeperfeito/login.html'
