from django.urls import path
from .views import mostrar_preguntas, detalles,home,crear_pregunta,crear_respuesta
urlpatterns = [
    
    path("preguntas/", mostrar_preguntas, name="preguntas" ),
    path("detalles/<int:question_id>/", detalles, name="detalles_por_pregunta" ),
    path("hacer_pregunta", crear_pregunta, name="formulario"),
    path("crear_respuesta/<int:pregunta_id>/", crear_respuesta, name="responder")

    
]