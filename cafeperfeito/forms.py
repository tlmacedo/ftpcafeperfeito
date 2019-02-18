from django import forms
from django.forms import TextInput
from passlib.handlers.django import django_pbkdf2_sha256

from cafeperfeito.models import *


class LoginForm(forms.ModelForm):
    class Meta:
        model = Usuario

        fields = [
            'email',
            'senha',
        ]

        widgets = {
            'senha': forms.PasswordInput(),
        }

    def valida_usuario(self):
        mailusuario = self.cleaned_data.get('email')
        nsenha = self.cleaned_data.get('senha')
        try:
            if not '@' in mailusuario:
                usuario = Usuario.objects.get(id=Colaborador.objects.get(apelido=mailusuario))
            else:
                usuario = Usuario.objects.get(email=mailusuario)
            if django_pbkdf2_sha256.verify(nsenha, usuario.senha) is True:
                print('Senha Validada com sucesso!!!!!!!!!!!!!!!!!!!!!!!!')
                # stream = io.BytesIO(usuario.id.imgcolaborador)
                # img = Image.open(stream)
                # img.save('static/cafeperfeito/img/user.png')
                return usuario
            else:
                print('Senha inválida')
                return False
        except Colaborador.DoesNotExist or Usuario.DoesNotExist:
            return None
        pass


class ProdutoForm(forms.ModelForm):
    # id = forms.CharField(
    #     label='Pkd',
    #     widget=forms.TextInput(
    #         attrs={
    #             'readonly': 'readonly',
    #             'class': 'text-right',
    #         }),
    # )
    codigo = forms.CharField(
        label='codigoteste',
        max_length=15,
        required='True',
        widget=forms.TextInput(
            attrs={
                'class': 'text-right msk-telefone',
            }),
    )
    descricao = forms.CharField(
        label='Descrição',
        max_length=120,
    )
    peso = forms.DecimalField(
        label='Peso',
        max_digits=19,
        decimal_places=3,
    )
    unidadecomercial = forms.ChoiceField(
        label='Und Comercial',
        choices=UNIDADE_COMERCIAL.choices(),
    )
    situacao = forms.ChoiceField(
        label='Situação',
        choices=SITUACAO_NO_SISTEMA.choices(),
    )
    precofabrica = forms.DecimalField(
        label='vlr fabrica',
        max_digits=19,
        decimal_places=2,
    )
    precoconsumidor = forms.DecimalField(
        label='vlr Consumidor',
        max_digits=19,
        decimal_places=2,
    )
    varejo = forms.IntegerField(
        label='varejo',
        max_value=99,
    )
    ultimpostosefaz = forms.DecimalField(
        label='vlr Sefaz',
        max_digits=19,
        decimal_places=2,
    )
    ultfrete = forms.DecimalField(
        label='vlr frete',
        max_digits=19,
        decimal_places=2,
    )
    comissao = forms.DecimalField(
        label='comissão %',
        max_digits=19,
        decimal_places=2,
    )
    ncm = forms.CharField(
        label='ncm',
        # max_length=8,
        widget=TextInput(attrs={'class': 'mask-ncm'})
        # blank=True,
        # null=True,
    )
    cest = forms.CharField(
        label='cest',
        max_length=7,
        # blank=True,
        # null=True,
    )
    fiscalcstorigem = forms.ModelChoiceField(
        label='cst origem',
        queryset=FiscalCstOrigem.objects.all(),
        # blank=True,
        # null=True,
    )
    fiscalicms = forms.ModelChoiceField(
        label='icms',
        queryset=FiscalIcms.objects.all(),
        # blank=True,
        # null=True,
    )
    fiscalpis = forms.ModelChoiceField(
        label='pis',
        queryset=FiscalPisCofins.objects.all(),
        # blank=True,
        # null=True,
    )
    fiscalcofins = forms.ModelChoiceField(
        label='cofins',
        queryset=FiscalPisCofins.objects.all(),
        # blank=True,
        # null=True,
    )
    nfegenero = forms.CharField(
        label='gênero',
        max_length=255,
        # blank=True,
        # null=True,
    )
    usuariocadastro = forms.CharField(
        label='usuario cadastro',
        max_length=40,
        # blank=True,
        # null=True,
    )
    datacadastro = forms.CharField(
        label='data cadastro',
    )

    # usuarioatualizacao = forms.CharField(
    #     label='usuario atualização',
    #     max_length=40,
    #     # queryset=Usuario.objects.all(),
    #     # blank=True,
    #     # null=True,
    # )
    # dataatualizacao = forms.CharField(
    #     label='data atualização',
    # )
    #
    # imgproduto = forms.ImageField(
    #     label='imagem produto',
    # )

    class Meta:
        model = Produto

        fields = '__all__'

        # fields = (
        #     'id', 'codigo', 'descricao', 'peso', 'unidadecomercial', 'situacao', 'precofabrica',
        #     'precoconsumidor', 'varejo', 'ultimpostosefaz', 'ultfrete', 'comissao', 'ncm',
        #     'cest', 'fiscalcstorigem', 'fiscalicms', 'fiscalpis', 'fiscalcofins', 'nfegenero',
        #     'usuariocadastro', 'usuarioatualizacao',
        # )
        # widgets = {
        #     'id': TextInput(attrs={'readonly': 'readonly', 'class': 'text-right'}),
        #     'name': TextInput(attrs={'class': 'text-right', 'rows': 20}),
        # }
