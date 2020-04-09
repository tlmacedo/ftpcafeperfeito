from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, UpdateView
from django.views.generic.list import ListView

from cafeperfeito.forms import LoginForm
from cafeperfeito.models import Usuario


class LoginTemplateView(FormView):
    model = Usuario
    form_class = LoginForm
    template_name = 'cafeperfeito/login.html'
