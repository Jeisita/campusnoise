from django.urls import path
from .views import (
    LugarListView,
    LugarDetailView,
    LugarCreateView,
    LugarUpdateView,
    LugarDeleteView,
    ReporteCreateView
)

urlpatterns = [
    path('', LugarListView.as_view(), name='home'),

    path('lugar/<int:pk>/',
         LugarDetailView.as_view(),
         name='detalle_lugar'),

    path('lugar/nuevo/',
         LugarCreateView.as_view(),
         name='crear_lugar'),

    path('lugar/<int:pk>/editar/',
         LugarUpdateView.as_view(),
         name='editar_lugar'),

    path('lugar/<int:pk>/eliminar/',
         LugarDeleteView.as_view(),
         name='eliminar_lugar'),

    path('reporte/nuevo/',
         ReporteCreateView.as_view(),
         name='crear_reporte'),
]