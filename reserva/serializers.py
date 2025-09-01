from rest_framework import serializers
#Importamos los modelos de la app
from .models import EstadoReserva,Reserva



class EstadoReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoReserva
        fields = '__all__'



class ReservaSerializer(serializers.ModelSerializer):
    class Meta:

        model = Reserva
        fields = '__all__'