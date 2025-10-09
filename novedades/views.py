from django.shortcuts import render
from .models import Novedad

from django.core.paginator import Paginator # importar el paginador


# def nov(request):
#     novedad = Novedad.objects.all()
#     return render(request, "nov/novedades.html", {'novedad': novedad})


def nov(request):
    noved = Paginator(Novedad.objects.all(), 2) # 2 novedades por pagina
    nov_number = request.GET.get("page") # obtener el numero de pagina
    novedad = noved.get_page(nov_number) # obtener la pagina

    return render(request, "nov/novedades.html", {'novedad': novedad}) # pasar la pagina al template
