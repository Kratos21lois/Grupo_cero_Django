from django.shortcuts import render
from .models import Autor

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def prueba(request):
        todos_autores = Autor.objects.all()
        datos = {"todosA" : todos_autores}


        return render(request, "core/prueba.html", datos)

