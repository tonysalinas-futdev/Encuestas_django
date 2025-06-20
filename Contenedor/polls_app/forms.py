from django.forms import ModelForm
from polls_app.models import Question, Respuesta
class PreguntaForm(ModelForm):
    class Meta:
        model=Question
        fields=["pregunta"]

class RespuestaForm(ModelForm):
    class Meta:
        model=Respuesta
        fields=["respuesta"]