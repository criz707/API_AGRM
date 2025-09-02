from rest_framework import serializers
#Importamos los modelos de la app
from .models import Rol,Usuario



class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'



class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:

        
        model = Usuario
        fields= [
            'id',
            'nombre',
            'correo',
            'foto',
            'contrasena',
            'rol'
        ]
        #Serialiadores anidados
        




    #Validaciones
    def validate(self,attrs):
        if (len(attrs["contrasena"]) < 5  and "@dreamland.com" not in attrs['correo']):
            raise serializers.ValidationError("La contraseña es muy corta y el correo no contiene @dreamland.com :D")

    def validate_correo(self,value):
        # value = "hola@dreamland.com"
        if "@dreamland.com" in value:

            return value
        raise serializers.ValidationError("El correo debe incluir@dreamland.com :D")
    

