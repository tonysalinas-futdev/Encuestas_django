from django.urls import path
from .views import mostrar_preguntas, detalles,home
urlpatterns = [
    path("preguntas/", mostrar_preguntas, name="preguntas" ),
    path("detalles/<int:question_id>/", detalles, name="detalles_por_pregunta" ),
    path("", home , name="home")
]