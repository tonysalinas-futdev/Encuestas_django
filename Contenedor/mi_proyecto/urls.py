
from django.contrib import admin
from django.urls import path, include
from polls_app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="inicio" ),
    path("questions/", include("polls_app.urls"))
]
