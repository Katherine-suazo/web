from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [

    path('',views.home,name="home"),
    path('gallery/',views.gallery,name="gallery"),
    path('novedades/',views.novedades,name="novedades"),
    path('qsomos/',views.quienes_somos,name="qsomos"),
    
    path('admin/', admin.site.urls),
]


