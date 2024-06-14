import structlog
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

logger: structlog.BoundLogger = structlog.get_logger('webapp__views')


@login_required
def index(request: HttpRequest) -> HttpResponse:
    data = {'title': 'Главная', 'home': True}

    return render(request, 'index.html', data)
