from django.contrib import admin
from polls_app import models

admin.site.register(models.Question)
admin.site.register(models.Respuesta)

