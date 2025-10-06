from django.contrib import admin
from django.urls import path

from core import views as views_core
from novedades import views as views_novedades

from  django.conf import settings


urlpatterns = [

    path('',views_core.home,name="home"),
    path('gallery/',views_core.gallery,name="gallery"),
    path('qsomos/',views_core.quienes_somos,name="qsomos"),

    path('novedades/',views_novedades.nov,name="novedades"),
    
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

