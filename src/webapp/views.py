import structlog
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

logger: structlog.BoundLogger = structlog.get_logger('webapp__views')


@login_required
def index(request: HttpRequest) -> HttpResponse:
    data = {
        'title': 'Главная',
        'home': True,
        'income': {
            'value': 143200,
            'balance': 43200,
            'percent': 79,
            'trend_direction': True
        },
        'expenses': {
            'value': 34720,
            'balance': 2300,
            'percent': 1.2,
            'trend_direction': False
        },
        'deposits': {
            'value': 18400,
            'balance': 10240,
            'percent': 64.25,
            'trend_direction': False
        },
        'savings': {
            'value': 180000,
            'balance': 0,
            'percent': 100,
            'trend_direction': True
        }
    }

    return render(request, 'index.html', data)
