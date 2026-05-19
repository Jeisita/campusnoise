from django.contrib import admin
from .models import Lugar, ReporteRuido


@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edificio', 'tipo_espacio')
    search_fields = ('nombre',)


@admin.register(ReporteRuido)
class ReporteRuidoAdmin(admin.ModelAdmin):
    list_display = ('lugar', 'nivel_ruido', 'fecha')
    list_filter = ('nivel_ruido',)