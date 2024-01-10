from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.views import LoginView

User = get_user_model()

class UserCreationForm(UserCreationForm):

    email = forms.EmailField(
    label=_("Почта"),
    max_length=254,
    widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    password1 = forms.CharField(
        label=_("Пароль"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        
    )

    password2 = forms.CharField(
        label=_("Подтвердите пароль"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="",
    )

    username = forms.CharField(
        label=_("Имя пользователя"),
    )

    error_messages = {
        "password_mismatch": _("Два поля пароля не совпадают."),
    }
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")



class CostmeAuthenticationForm(AuthenticationForm):

    username = forms.CharField( label=_("Имя пользователя"))
    
    password = forms.CharField(
        label=_("Пароль"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

    error_messages = {
        'invalid_login': _(
            "Пожалуйста, введите правильное имя пользователя и пароль. Обратите внимание, что оба "
            "поля могут быть чувствительны к регистру."
        ),
        'inactive': _("This account is inactive."),
    }


class MyLoginView(LoginView):
    authentication_form = CostmeAuthenticationForm

