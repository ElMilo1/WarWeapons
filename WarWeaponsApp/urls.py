from django.urls import path , include
from WarWeaponsApp import views as Vista1
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Vista1.Home),
    path('registro/',Vista1.Registro),
    path('listar/',Vista1.Listar),
    path('borrar/<int:id>',Vista1.Borrar),
    path('editar/<int:id>',Vista1.Editar)
]