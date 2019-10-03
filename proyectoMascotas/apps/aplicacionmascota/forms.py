from django import forms
from .models import Mascota 

class Mascotaform(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = [
            'nombre'
            'raza'
            'edad'
            'persona'
        ]