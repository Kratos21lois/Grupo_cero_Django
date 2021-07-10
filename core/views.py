from django.shortcuts import render
from .models import Autor, Obra

# Create your views here.


def prueba(request):
        autores = Autor.objects.all()
        obras =   Obra.objects.all()
        datos = {"autores" : autores, "obras" : obras}
        
        return render(request, "core/prueba.html", datos)

