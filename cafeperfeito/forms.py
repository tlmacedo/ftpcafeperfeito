from django import forms

from cafeperfeito.models import Usuario


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
