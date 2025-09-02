from django.urls import path
from .views import ListRoles,DetalleUsuario,ListaUsuarios
from .viewsets import UsuarioViewSet,RolViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('usuario',UsuarioViewSet)
router.register('rol',RolViewSet)
urlpatterns = router.urls