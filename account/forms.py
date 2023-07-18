# Import all requirements
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login as DjangoLogin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UsernameField
from .models import user_accounts
from django.db.models import Q
from django.db import models
from django import forms


class LoginForm(AuthenticationForm):
    codeMelli = forms.CharField(
        label='کد ملی',
        widget=forms.TextInput(attrs={'placeholder': 'کد ملی'})
    )

    def clean(self):
        email = self.cleaned_data.get('email')
        codeMelli = self.cleaned_data.get('codeMelli')
        password = self.cleaned_data.get('password')

        if email and password and codeMelli:
            user = authenticate(request=self.request, username=email, codeMelli=codeMelli, password=password)
            if user is None:
                raise forms.ValidationError('اطلاعات وارد شده صحیح نیست')
            else:
                self.confirm_login_allowed(user)

        return self.cleaned_data