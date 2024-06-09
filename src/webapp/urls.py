from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from src.webapp import views

urlpatterns = [
    path('', views.index, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
