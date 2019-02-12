import datetime
from base64 import b64encode

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.views.generic.list import ListView

from cafeperfeito.forms import LoginForm
from cafeperfeito.service import bytes2image
from ftpcafeperfeito.models import Usuario, Produto

now = datetime.datetime.now()


class LoginTemplateView(FormView):
    form_class = LoginForm
    template_name = 'cafeperfeito/login.html'
    model = Usuario
    context_object_name = 'usuario'
    extra_context = {'now': now, }
    success_url = reverse_lazy('cafeperfeito:home')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
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
            return self.form_invalid(**{'form': form})
        return render(request, 'cafeperfeito/login.html', {'form': form})


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    login_url = '/'
    permission_denied_message = 'não está conectado'
    raise_exception = True
    redirect_field_name = 'next'

    extra_context = {'now': now}
    template_name = 'cafeperfeito/home.html'

    def post(self, request, *args, **kwargs):
        if request.FILES['logUserNewImagem']:
            logUsuario = Usuario.objects.get(id=self.request.user.id)
            f = request.FILES['logUserNewImagem']
            with open('cafeperfeito/static/cafeperfeito/img/name.png', 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
                    print(destination.name)
            # for line in upload:
            #     print(line)
            # path = upload.content_type
            # arquivo = upload.read()  # For small files
            # print('local:', upload)
            with open('cafeperfeito/static/cafeperfeito/img/name.png', 'rb') as file:
                bynaryData = file.read()
            print(bynaryData)
            logUsuario.id.imgcolaborador = bynaryData
            logUsuario.save()
            bytes2image(bynaryData)
            return render(request, self.template_name)

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        logUsuario = Usuario.objects.get(id=self.request.user.id)
        context['logUser'] = logUsuario
        # context['logUserImagem'] = b64encode(logUsuario.id.imgcolaborador).decode('ascii')

        return context


class ProdutosListView(LoginRequiredMixin, ListView):
    login_url = '/'
    permission_denied_message = 'não está conectado'
    raise_exception = True
    redirect_field_name = 'next'

    extra_context = {'now': now}
    model = Produto
    context_object_name = 'produtos'
    template_name = 'cafeperfeito/produtos.html'

    def get_context_data(self, **kwargs):
        context = super(ProdutosListView, self).get_context_data()
        logUsuario = Usuario.objects.get(id=self.request.user.id)
        context['logUser'] = logUsuario
        context['logUserImagem'] = b64encode(logUsuario.id.imgcolaborador).decode('ascii')

        return context
