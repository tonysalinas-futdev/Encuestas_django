from django.db import models

class Question(models.Model):
    pregunta=models.CharField(max_length=1500)
    fecha_publicacion=models.DateTimeField(auto_now_add=True)    
    
    def __str__(self):
        return self.pregunta


class Respuesta(models.Model):
    respuesta=models.TextField(max_length=2000)
    fecha=models.DateTimeField(auto_now_add=True)
    question=models.ForeignKey(Question, on_delete=models.CASCADE, related_name="respuestas")