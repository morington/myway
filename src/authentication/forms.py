import structlog
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

logger: structlog.BoundLogger = structlog.get_logger(__name__)


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', error_messages={'required': 'Поле обязательно для заполнения'})
    password = forms.CharField(label='Пароль', error_messages={'required': 'Поле обязательно для заполнения'})
    error_messages = {'invalid_login': "Неверный логин или пароль"}

    def clean_username(self):
        username = self.cleaned_data['username']
        user_model = get_user_model()
        _user = user_model.objects.filter(login=username)

        return username
