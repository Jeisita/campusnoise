from django.test import TestCase
from django.urls import reverse

from .models import Lugar
from .forms import ReporteRuidoForm


class LugarModelTest(TestCase):

    def test_creacion_lugar(self):

        lugar = Lugar.objects.create(
            nombre='Biblioteca Norte',
            edificio='Edificio B',
            tipo_espacio='Biblioteca',
            descripcion='Zona tranquila'
        )

        self.assertEqual(lugar.nombre, 'Biblioteca Norte')


class HomeViewTest(TestCase):

    def test_home_view_status_code(self):

        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)


class ReporteFormTest(TestCase):

    def test_formulario_reporte_valido(self):

        lugar = Lugar.objects.create(
            nombre='Sala 101',
            edificio='Edificio C',
            tipo_espacio='Sala',
            descripcion='Sala de estudio'
        )

        form = ReporteRuidoForm(data={
            'lugar': lugar.id,
            'nivel_ruido': 'Bajo',
            'ocupacion': 10,
            'wifi': True
        })

        self.assertTrue(form.is_valid())