import datetime

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from cafeperfeito.forms import LoginForm
from ftpcafeperfeito.models import Usuario

now = datetime.datetime.now()


class LoginTemplateView(FormView):
    form_class = LoginForm
    template_name = 'cafeperfeito/login.html'
    model = Usuario
    context_object_name = 'usuario'
    extra_context = {'now': now, }
    success_url = reverse_lazy('cafeperfeito:home')
    error_message = 'Deu zebra meu filho'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            #     user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['senha'])
            #     login(request, user)
            #     print(user.email)
            #     # if user.is_authenticate:
            #     return self.form_valid(form)
            # else:
            #     return self.form_invalid(**{'form': form})

            usuario = form.valida_usuario()
            user = authenticate(username=usuario.id.apelido, password=form.cleaned_data['senha'])
            login(request, user)
            if user is None:
                messages.error(request, 'usuario não existe')
            else:
                if usuario is False:
                    messages.error(request, 'usuário ou senha invalido')
                else:
                    return self.form_valid(form)
                    # return HttpResponseRedirect(self.get_success_url(), {'form': form})
            return self.form_invalid(**{'form': form})
        return render(request, 'cafeperfeito/login.html', {'form': form})


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    login_url = '/'
    permission_denied_message = 'não está conectado'
    raise_exception = True
    redirect_field_name = 'next'

    extra_context = {'now': now}
    template_name = 'cafeperfeito/home.html'

    # def get_context_data(self, request, **kwargs):
    #     context = super(HomeTemplateView, self).get_context_data(**kwargs)
    #     context['usuario'] = Usuario.objects.get(id=self.request.user.id)
    #     return context

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        context['usuario'] = Usuario.objects.get(id=self.request.user.id)
        return context
    # def get(self, request, *args, **kwargs):
    #     context = super(HomeTemplateView, self).get_context_data(**kwargs)
    #     context['usuario'] = Usuario.objects.get(id=request.user.id)
    #     return context


class EmpresaTemplateView(TemplateView):
    template_name = 'cafeperfeito/empresa.html'
