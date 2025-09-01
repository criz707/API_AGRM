from django.urls import path
from .viewsets import MesaViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('mesa',MesaViewSet)
urlpatterns = router.urls