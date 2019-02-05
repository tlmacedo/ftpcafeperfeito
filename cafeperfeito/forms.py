import bcrypt
from django import forms

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
            usuario = Usuario.objects.get(email=mailusuario)
            # if usuario is None:
            #     print('Usuario não existe')
            #     return None
            # else:
            if bcrypt.checkpw(str(nsenha).encode(), str(usuario.senha).encode()) is True:
                print('Senha Validade com sucesso!!!!!!!!!!!!!!!!!!!!!!!!')
                return usuario;
            else:
                print('Senha inválida')
                return False
        except Usuario.DoesNotExist:
            return None
        pass
