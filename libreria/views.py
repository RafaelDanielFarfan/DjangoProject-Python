from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import libro
from .forms import libroForm

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def libros(request):
    libros= libro.objects.all()
    return render(request, 'index.html', {'libros': libros})

def crear(request):
    formulario = libroForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')

    return render(request, 'crear.html', {'formulario':formulario})

def editar(request, id):
     
     libros=libro.objects.get(id=id)
     formulario = libroForm(request.POST or None, request.FILES or None, instance=libros)
     return render(request, 'editar.html')

def eliminar(request, id):
    libros=libros.objects.get(id=id)
    libros.delete()
    return redirect('libros')
