import datetime

import bcrypt
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from cafeperfeito.forms import LoginForm

now = datetime.datetime.now()


def senhaEncrypt(senha):
    return bcrypt.hashpw(senha, bcrypt.gensalt(10))


def senhaValida(senha, senha_db):
    return bcrypt.checkpw(senha, senha_db)


class LoginTemplateView(FormView):
    form_class = LoginForm
    template_name = 'cafeperfeito/login.html'
    success_url = reverse_lazy('cafeperfeito:principal')
    error_message = 'Deu zebra meu filho'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            usuario = form.valida_usuario()
            if usuario is None:
                messages.error(request, 'usuario não existe')
            else:
                if usuario is False:
                    messages.error(request, 'usuário ou senha invalido')
                else:
                    user = authenticate(username=usuario.id.apelido, password=form.cleaned_data['senha'])
                    login(request, user)
                    return HttpResponseRedirect(self.get_success_url(), {'usuario': usuario}, {'form': form})
            return render(request, 'cafeperfeito/login.html', {'form': form})
        else:
            print('aiaiai')

            #     user = authenticate(username=usuario.id.apelido, password=usuario.senha)
            #     login(request, user)
            #     # return self.form_valid(form)
            #     HttpResponseRedirect(self.get_success_url(), {'form': form})
            # else:
            #     # return self.form_invalid(**{'form': form})
            #     return render(request, 'cafeperfeito/login.html', {'form': form})


class PrincipalTemplateView(TemplateView):
    template_name = 'cafeperfeito/principal.html'


class EmpresaTemplateView(TemplateView):
    template_name = 'cafeperfeito/empresa.html'
