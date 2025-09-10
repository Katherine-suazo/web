from django.contrib import admin
from django.urls import path
from core import views  #AÑADIR ESTO ---------------

urlpatterns = [

    path('',views.home,name="home"),
    path('gallery/',views.gallery,name="gallery"),
    path('novedades/',views.novedades,name="novedades"),
    path('qsomos/',views.quienes_somos,name="qsomos"),
    
    path('admin/', admin.site.urls),
]

# se definen todas las rutas de la aplicacion core
# la ruta vacia '' es la pagina de inicio y se conecta con la vista home en core/views.py
# la ruta 'gallery/' se conecta con la vista gallery en core/views.py
# la ruta 'admin/' es para el panel de administracion de Django

