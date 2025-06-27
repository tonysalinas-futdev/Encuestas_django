from django.forms import ModelForm
from polls_app.models import Question, Respuesta
class PreguntaForm(ModelForm):
    class Meta:
        model=Question
        fields=["pregunta"]
        labels={"pregunta": ("Escriba su pregunta."),}
        help_texts={
            "pregunta": ("Trate de que la pregunta no exceda los 1000 caracteres")
        }
        error_messages={
            "pregunta": {"max_length":"La pregunta es demasiado larga",
                        "required": "Este campo es obligatorio"}

            
        }

class RespuestaForm(ModelForm):
    class Meta:
        model=Respuesta
        fields=["respuesta"]