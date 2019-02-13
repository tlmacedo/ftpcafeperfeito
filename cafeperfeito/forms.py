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


class InsereProdutoForm(forms.ModelForm):
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
        max_length=120
    )
    peso = forms.DecimalField(
        label='Peso',
        max_digits=19,
        decimal_places=3,

    )
    # unidadecomercial = forms.ModelChoiceField(queryset=None,
    #     # choices=UNIDADE_COMERCIAL.choices()
    # )  # .IntegerField(db_column='unidadeComercial')  # Field name made lowercase.
    # situacao = forms.ModelChoiceField(queryset=None,
    #     # choices=SITUACAO_NO_SISTEMA.choices()
    # )  # .IntegerField()

    # precofabrica = forms.DecimalField(db_column='precoFabrica', max_digits=19,
    #                                   decimal_places=2)  # Field name made lowercase.
    # precoconsumidor = forms.DecimalField(db_column='precoConsumidor', max_digits=19,
    #                                      decimal_places=2)  # Field name made lowercase.
    # varejo = forms.IntegerField()
    # ultimpostosefaz = forms.DecimalField(db_column='ultImpostoSefaz', max_digits=19,
    #                                      decimal_places=2)  # Field name made lowercase.
    # ultfrete = forms.DecimalField(db_column='ultFrete', max_digits=19, decimal_places=2)  # Field name made lowercase.
    # comissao = forms.DecimalField(max_digits=19, decimal_places=2)
    # ncm = forms.CharField(max_length=8, blank=True, null=True)
    # cest = forms.CharField(max_length=7, blank=True, null=True)
    # fiscalcstorigem = forms.ForeignKey(Fiscalcstorigem, forms.DO_NOTHING, db_column='fiscalCstOrigem_id', blank=True,
    #                                    null=True)  # Field name made lowercase.
    # fiscalicms = forms.ForeignKey(Fiscalicms, forms.DO_NOTHING, db_column='fiscalIcms_id', blank=True,
    #                               null=True)  # Field name made lowercase.
    # fiscalpis = forms.ForeignKey(Fiscalpiscofins, forms.DO_NOTHING, related_name='fiscalpis',
    #                              db_column='fiscalPis_id', blank=True,
    #                              null=True)  # Field name made lowercase.
    # fiscalcofins = forms.ForeignKey(Fiscalpiscofins, forms.DO_NOTHING, related_name='fiscalcofins',
    #                                 db_column='fiscalCofins_id', blank=True,
    #                                 null=True)  # Field name made lowercase.
    # nfegenero = forms.CharField(db_column='nfeGenero', max_length=255, blank=True,
    #                             null=True)  # Field name made lowercase.
    # usuariocadastro = forms.ForeignKey('Usuario', forms.DO_NOTHING, related_name='usuariocadastroproduto',
    #                                    db_column='usuarioCadastro_id', blank=True,
    #                                    null=True)  # Field name made lowercase.
    # datacadastro = forms.DateTimeField(db_column='dataCadastro', auto_now_add=True)  # Field name made lowercase.
    # usuarioatualizacao = forms.ForeignKey('Usuario', forms.DO_NOTHING, related_name='usuarioatualizacaoproduto',
    #                                       db_column='usuarioAtualizacao_id', blank=True,
    #                                       null=True)  # Field name made lowercase.
    # dataatualizacao = forms.DateTimeField(db_column='dataAtualizacao', blank=True,
    #                                       null=True, auto_now=True)  # Field name made lowercase.
    # imgproduto = forms.BinaryField(db_column='imgProduto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        model = Produto

        fields = '__all__'
