import os

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, UpdateView
from django.views.generic.list import ListView

from cafeperfeito.forms import LoginForm, ProdutoForm
from cafeperfeito.models import Usuario, Produto, Colaborador, AuthUser, ProdutoCodigoBarra
from cafeperfeito.service import image2bytes, blob2base64


class LoginTemplateView(FormView):
    model = Usuario
    form_class = LoginForm
    template_name = 'cafeperfeito/login.html'
    success_url = reverse_lazy('cafeperfeito:home')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            usuario = form.valida_usuario()
            if usuario is None:
                messages.info(request, 'usuario não existe')
            else:
                if usuario is False:
                    messages.error(request, 'usuário ou senha invalido')
                else:
                    userDjango = AuthUser.objects.get(id=usuario.id.id)
                    user = authenticate(username=userDjango.username, password=form.cleaned_data['senha'])
                    login(request, user)
                    return self.form_valid(form)
            return self.form_invalid(**{'form': form})


def gera_context(usuario, context):
    context['meuUsuario'] = usuario
    context['userImagem'] = blob2base64(usuario.id.imagem)
    return context


def get_imagemPrdotudo(produto, context):
    context['produto'] = produto
    context['produtoImagem'] = blob2base64(produto.imgproduto)
    return context


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    login_url = '/'

    template_name = 'cafeperfeito/home.html'

    def get_context_data(self, **kwargs):
        return gera_context(Usuario.objects.get(id=self.request.user.id),
                            super(HomeTemplateView, self).get_context_data(**kwargs))


class ProdutosListView(LoginRequiredMixin, ListView):
    login_url = '/'

    template_name = 'cafeperfeito/produtos.html'
    model = Produto

    context_object_name = 'produtos'

    # def get(self, request, *args, **kwargs):
    #
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         form.atualiza_img_produtos

    def get_context_data(self, *, object_list=None, **kwargs):
        context = gera_context(Usuario.objects.get(id=self.request.user.id),
                               super(ProdutosListView, self).get_context_data())
        # print(atualiza_img_produtos())
        return context


class ProdutoCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'

    template_name = 'cafeperfeito/produto_cadastrar.html'
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('cafeperfeito:lista_produtos')

    def get_context_data(self, **kwargs):
        return gera_context(Usuario.objects.get(id=self.request.user.id),
                            super(ProdutoCreateView, self).get_context_data())


class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'

    template_name = 'cafeperfeito/produto_atualizar.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('cafeperfeito:lista_produtos')

    def get_context_data(self, **kwargs):
        context = gera_context(Usuario.objects.get(id=self.request.user.id),
                               super(ProdutoUpdateView, self).get_context_data())
        return get_imagemPrdotudo(self.object, context)

    def get_object(self, queryset=None):
        produto = None

        id = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if id is not None:
            produto = Produto.objects.filter(id=id).first()
        elif slug is not None:
            campo_slug = self.get_slug_field()
            produto = Produto.objects.filter(**{campo_slug: slug}).first()

        # produto.imgproduto = image2bytes("/Users/thiagomacedo/Desktop/supremoArabica.png")
        # produto.save(update_fields=['imgproduto'])

        return produto


def atualiza_img_produtos():
    produtos = Produto.objects.all()
    path = "/Users/thiagomacedo/Desktop/MySqlTestes/"
    types = ['.jpeg', '.jpg', '.png']
    for prod in produtos:
        prod.imgproduto = None
        print('produto: {}'.format(prod.descricao))
        try:
            codBarra = ProdutoCodigoBarra.objects.get(produto_id=prod.id)
            if codBarra is not None:
                print('\tcodBarra0: [{}]'.format(codBarra.codigobarra))
                for file in os.listdir(path):
                    if file.__contains__(codBarra.codigobarra):
                        for type in types:
                            if file.endswith(codBarra.codigobarra + type):
                                print('\tfilesImg0: [{}]'.format(file))
                                prod.imgproduto = image2bytes(path + file)
                                print('\timg: [{}]'.format(prod.imgproduto))
                                # continue
                if prod.imgproduto is None:
                    print('\tfilesImg1: [{}]\n\timg: [{}]'.format('sem arquivo', 'sem imagem'))
        except:
            print('\tcodBarra1: [{}]'.format('sem código barras'))
        print('\n')
        prod.save(update_fields=['imgproduto'])
    return '\nOK terminamos'
