from django.urls import path
from .viewsets import ReservaViewSet,EstadoReservaViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('reserva',ReservaViewSet)
router.register('estadoreserva',EstadoReservaViewSet)
urlpatterns = router.urls