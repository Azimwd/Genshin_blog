from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class UserCreationForm(UserCreationForm):

    email = forms.EmailField(
    label=_("Имя пользователя"),
    max_length=254,
    widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
