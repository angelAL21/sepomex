from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', include('info_app.urls')), #info url para la consulta de info.
]
