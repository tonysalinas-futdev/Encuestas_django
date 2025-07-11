from django.shortcuts import render, get_object_or_404, redirect
from polls_app import models
from polls_app.forms import PreguntaForm, RespuestaForm    
from django.contrib import messages
def home(request):
    ultimas_preguntas=models.Question.objects.all().order_by("-fecha_publicacion")[:5]
    return render(request, "index.html",{"preguntas":ultimas_preguntas})

def mostrar_preguntas(request):
    preguntas=models.Question.objects.all().order_by("fecha_publicacion")

    return render(request, "preguntas.html",{
        "preguntas":preguntas
    })

def detalles(request,question_id):
    #Obtengo la pregunta con ese Id
    todas_las_preguntas=get_object_or_404(models.Question,id=question_id)
    #Obtengo todas las respuestas de esa pregunta
    respuestas=todas_las_preguntas.respuestas.all().order_by("-votos")

    return render(request, "detalles.html",{"respuestas": respuestas,
                                            "preguntas":todas_las_preguntas})

def crear_pregunta(request):
    if request.method=="POST":
        form=PreguntaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Pregunta enviada correctamente")

            return redirect("inicio")
    else:
        form=PreguntaForm()
    return render(request, "crear_pregunta.html", {"form":form})



def crear_respuesta(request, pregunta_id):
    pregunta = get_object_or_404(models.Question, id=pregunta_id)
    if request.method == "POST":
        form = RespuestaForm(request.POST)
        if form.is_valid():
            respuesta = form.save(commit=False)
            respuesta.question = pregunta  # Asocia la respuesta a la pregunta
            respuesta.save()
            return redirect("inicio")
    else:
        form = RespuestaForm()
    return render(request, "responder.html", {"form": form, "pregunta": pregunta})


def votar_respuesta(request, respuesta_id):
    respuesta=get_object_or_404(models.Respuesta, id=respuesta_id)
    if request.method=="POST":
        respuesta.votos+=1
        respuesta.save()
    return redirect ("detalles_por_pregunta",question_id=respuesta.question_id )
        



def responder_respuesta(request, respuesta_id):
    pregunta = get_object_or_404(models.Respuesta, id=respuesta_id)
    if request.method == "POST":
        form = RespuestaForm(request.POST)
        if form.is_valid():
            respuesta = form.save(commit=False)
            respuesta.parent =respuesta
            respuesta.save()
            return redirect(request.META.get("HTTP_REFERER", "detalles"))
    else:
        form = RespuestaForm()
    return render(request, "responder.html", {"form": form, "respuesta": respuesta})