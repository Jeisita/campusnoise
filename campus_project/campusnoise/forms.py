from django import forms
from .models import Lugar, ReporteRuido


class LugarForm(forms.ModelForm):
    class Meta:
        model = Lugar
        fields = ['nombre', 'edificio', 'tipo_espacio', 'descripcion']


class ReporteRuidoForm(forms.ModelForm):
    class Meta:
        model = ReporteRuido
        fields = ['lugar', 'nivel_ruido', 'ocupacion', 'wifi']