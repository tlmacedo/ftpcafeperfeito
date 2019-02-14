from django import forms
from passlib.handlers.django import django_pbkdf2_sha256

from ftpcafeperfeito.models import *


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
                # colaborador = Colaborador.objects.get(apelido=mailusuario)
                usuario = Usuario.objects.get(id=Colaborador.objects.get(apelido=mailusuario))
            else:
                usuario = Usuario.objects.get(email=mailusuario)
            if django_pbkdf2_sha256.verify(nsenha, usuario.senha) is True:
                print('Senha Validada com sucesso!!!!!!!!!!!!!!!!!!!!!!!!')
                return usuario;
            else:
                print('Senha inválida')
                return False
        except Usuario.DoesNotExist:
            return None
        pass


class ProdutoForm(forms.ModelForm):
    id = forms.IntegerField(
        label='id',
        min_value=0,
    )
    codigo = forms.CharField(
        label='Código',
        max_length=15,
        required=True,
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
        max_length=8,
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
    usuariocadastro = forms.ModelChoiceField(
        label='usuario cadastro',
        queryset=Usuario.objects.all(),
        # blank=True,
        # null=True,
    )
    datacadastro = forms.DateTimeField(
        label='data cadastro',
    )
    usuarioatualizacao = forms.ModelChoiceField(
        label='usuario atualização',
        queryset=Usuario.objects.all(),
        # blank=True,
        # null=True,
    )
    dataatualizacao = forms.DateTimeField(
        label='data atualização',
    )
    imgproduto = forms.ImageField(
        label='imagem produto',
    )

    class Meta:
        model = Produto

        fields = '__all__'
