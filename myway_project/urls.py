from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('users/', include('src.authentication.urls', namespace="users")),
    path('', include('src.webapp.urls')),
]
