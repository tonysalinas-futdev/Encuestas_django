from django.urls import path
from .views import mostrar_preguntas, detalles
urlpatterns = [
    path("preguntas/", mostrar_preguntas, name="questions" ),
    path("detalles/<int:question_id>/", detalles, name="detallitos" )
]