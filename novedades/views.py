from django.shortcuts import render
from .models import Novedad

# Create your views here.

def nov(request):
    novedad = Novedad.objects.all()
    return render(request, "nov/novedades.html", {'novedad': novedad})
