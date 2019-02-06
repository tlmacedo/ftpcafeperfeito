from django import forms
from passlib.handlers.django import django_pbkdf2_sha256

from ftpcafeperfeito.models import *


class LoginForm(forms.ModelForm):
    # email = forms.CharField(
    #     required=True,
    #     label='Meu Email',
    #     max_length=120
    # )
    #
    # senha = forms.CharField(
    #     required=True,
    #     label="Minha Senha",
    #     max_length=15
    # )
    class Meta:
        model = Usuario

        fields = [
            'email',
            'senha'
        ]

        widgets = {
            'senha': forms.PasswordInput()
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
