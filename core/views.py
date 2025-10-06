from django.shortcuts import render

def home(request):
    return render(request,"core/home.html")

def gallery(request):
    return render(request,"core/gallery.html") 

# def novedades(request):
#     return render(request,"core/novedades.html")

def quienes_somos(request):
    return render(request, "core/qsomos.html")