from django import forms

from ftp_v201.models import Usuario


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
