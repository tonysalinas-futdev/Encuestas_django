from django.shortcuts import render, get_object_or_404
from polls_app import models
def home(request):
    return render(request, "index.html")
def mostrar_preguntas(request):
    preguntas=models.Question.objects.all().order_by("fecha_publicacion")

    return render(request, "preguntas.html",{
        "preguntas":preguntas
    })

def detalles(request,question_id):
    #Obtengo la pregunta con ese Id
    todas_las_preguntas=get_object_or_404(models.Question,id=question_id)
    #Obtengo todas las respuestas de esa pregunta
    respuestas=todas_las_preguntas.respuestas.all()

    return render(request, "detalles.html",{"respuestas": respuestas,
                                            "preguntas":todas_las_preguntas})

