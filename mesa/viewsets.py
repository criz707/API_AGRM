from rest_framework.viewsets import ModelViewSet
from .serializers import MesaSerializer
from .models import Mesa



class MesaViewSet(ModelViewSet):
    serializer_class = MesaSerializer
    queryset = Mesa.objects.all()