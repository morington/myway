from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse


@login_required
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Hello World!</h1>")
