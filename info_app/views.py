from django.shortcuts import render
from info_app.models import Info 
from django.http import JsonResponse

#obteniendo todos los municipios que se han agregado en el db en formato json.
def info_list(request):
    infos = Info.objects.all()
    data = {'municipios': list(infos.values())
        }
    
    
    return JsonResponse(data)