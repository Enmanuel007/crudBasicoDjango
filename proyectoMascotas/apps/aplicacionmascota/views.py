from django.shortcuts import render, redirect
from .models import Persona, Mascota
from .forms import Mascotaform


def home(request):
    return render(request, 'index.html')

def crearMascota(request):
    if request.method == 'POST':
        
        form = Mascotaform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:

        form = Mascotaform()
    return render(request,'aplicacionmascota/crear_mascota.html',{'form':form})


