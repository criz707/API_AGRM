from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('',include('docs.urls')),
    path('api-auth',include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('usuario.urls')),


    path('api/', include('mesa.urls')),
    path('api/', include('reserva.urls')),

    path('api/', include('reserva.urls')),
]