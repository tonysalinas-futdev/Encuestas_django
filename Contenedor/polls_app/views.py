from django.shortcuts import render
from polls_app import models

def mostrar_preguntas(request):
    preguntas=models.Question.objects.all().order_by("fecha_publicacion")

    return render(request, "preguntas.html",{
        "preguntas":preguntas
    })

def detalles(request,question_id):
    #Obtengo la pregunta con ese Id
    preguntas=models.Question.objects.get(id=question_id)
    #Obtengo todas las respuestas de esa pregunta
    respuestas=preguntas.respuestas.all()

    return render(request, "detalles.html",{"respuestas": respuestas,
                                            "pregunta":preguntas})

    