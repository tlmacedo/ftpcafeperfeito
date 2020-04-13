from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, UpdateView
from django.views.generic.list import ListView

from cafeperfeito.forms import LoginForm, ProdutoForm
from cafeperfeito.models import Usuario, Produto, Colaborador, AuthUser


class LoginTemplateView(FormView):
    model = Usuario
    form_class = LoginForm
    template_name = 'cafeperfeito/login.html'
    success_url = reverse_lazy('cafeperfeito:home')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            usuario = form.valida_usuario()
            userDjango = AuthUser.objects.get(id=usuario.id.id)
            if usuario is None:
                messages.info(request, 'usuario não existe')
            else:
                if usuario is False:
                    messages.error(request, 'usuário ou senha invalido')
                else:
                    user = authenticate(username=userDjango.username, password=form.cleaned_data['senha'])
                    login(request, user)
                    return self.form_valid(form)
            return self.form_invalid(**{'form': form})


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    login_url = '/'

    template_name = 'cafeperfeito/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        meuUsuario = Usuario.objects.get(id=self.request.user.id)
        context['meuUsuario'] = meuUsuario
        context['userImagem'] = meuUsuario.id.get_colaborador_imagem()
        return context


class ProdutosListView(LoginRequiredMixin, ListView):
    login_url = '/'

    template_name = 'cafeperfeito/produtos.html'
    model = Produto
    context_object_name = 'produtos'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProdutosListView, self).get_context_data()
        context['userImagem'] = Colaborador.objects.get(id=self.request.user.id).get_colaborador_imagem()
        return context


class ProdutoCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'

    template_name = 'cafeperfeito/produto_cadastrar.html'
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('cafeperfeito:lista_produtos')

    def get_context_data(self, **kwargs):
        context = super(ProdutoCreateView, self).get_context_data()
        context['userImagem'] = Colaborador.objects.get(id=self.request.user.id).get_colaborador_imagem()
        return context


class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'

    template_name = 'cafeperfeito/produto_atualizar.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('cafeperfeito:lista_produtos')

    def get_context_data(self, **kwargs):
        context = super(ProdutoUpdateView, self).get_context_data()
        context['userImagem'] = Colaborador.objects.get(id=self.request.user.id).get_colaborador_imagem()
        return context

    def get_object(self, queryset=None):
        produto = None

        id = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)

        if id is not None:
            produto = Produto.objects.filter(id=id).first()
        elif slug is not None:
            campo_slug = self.get_slug_field()
            produto = Produto.objects.filter(**{campo_slug: slug}).first()
        return produto
