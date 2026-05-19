from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Lugar, ReporteRuido


class LugarListView(ListView):
    model = Lugar
    template_name = 'home.html'
    context_object_name = 'lugares'


class LugarDetailView(DetailView):
    model = Lugar
    template_name = 'lugar_detail.html'
    context_object_name = 'lugar'


class LugarCreateView(CreateView):
    model = Lugar
    fields = ['nombre', 'edificio', 'tipo_espacio', 'descripcion']
    template_name = 'lugar_form.html'
    success_url = reverse_lazy('home')


class LugarUpdateView(UpdateView):
    model = Lugar
    fields = ['nombre', 'edificio', 'tipo_espacio', 'descripcion']
    template_name = 'lugar_form.html'
    success_url = reverse_lazy('home')


class LugarDeleteView(DeleteView):
    model = Lugar
    template_name = 'lugar_confirm_delete.html'
    success_url = reverse_lazy('home')


class ReporteCreateView(CreateView):
    model = ReporteRuido
    fields = ['lugar', 'nivel_ruido', 'ocupacion', 'wifi']
    template_name = 'reporte_form.html'
    success_url = reverse_lazy('home')