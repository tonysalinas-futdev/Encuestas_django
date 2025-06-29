from django.urls import path
from .views import mostrar_preguntas, detalles,crear_pregunta,crear_respuesta, votar_respuesta, responder_respuesta
urlpatterns = [
    
    path("preguntas/", mostrar_preguntas, name="preguntas" ),
    path("detalles/<int:question_id>/", detalles, name="detalles_por_pregunta" ),
    path("hacer_pregunta", crear_pregunta, name="formulario"),
    path("crear_respuesta/<int:pregunta_id>/", crear_respuesta, name="responder"),
    path("votar_respuesta/<int:respuesta_id>/", votar_respuesta, name="votar_respuesta"),
    path("responder_respuesta/<int:respuesta_id>/", responder_respuesta, name="responder_respuesta")
    
]