from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserModel


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = UserModel
        fields = ("username", 'first_name', 'last_name', 'password1',
                  'balance', 'bonus', 'password2', 'email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email',
                  'balance', 'bonus', 'password',)
