from django.urls import path
from info_app.views import info_list



urlpatterns = [
    path('list/', info_list, name= 'municipio-list'), #listará los municipios de la db.
]
