import structlog
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse

from src.authentication.forms import LoginUserForm
from myway_project.settings import REMEMBER_TIME

logger: structlog.BoundLogger = structlog.get_logger(__name__)


class LoginUser(LoginView):
    form_class = LoginUserForm
    extra_context = {'title': 'Вход'}
    template_name = 'login.html'

    def form_valid(self, form):
        remember_me = form.data.get('remember_me', None)
        self.request.session.modified = True

        if remember_me is not None:
            self.request.session.set_expiry(REMEMBER_TIME)
        else:
            self.request.session.set_expiry(0)

        return super(LoginUser, self).form_valid(form)


def logout_user(request: HttpRequest) -> HttpResponse:
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))
