from django import forms
from django.contrib.auth.forms import UserCreationForm, password_validation
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

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

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
