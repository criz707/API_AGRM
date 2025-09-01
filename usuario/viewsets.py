from rest_framework.viewsets import ModelViewSet
from .serializers import UsuarioSerializer
from .models import Usuario,Rol
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsRecepcionista 
from rest_framework import status




class UsuarioViewSet(ModelViewSet):    
    serializer_class = UsuarioSerializer

    queryset = Usuario.objects.all()
    #Ejemplo de metodo de agendar reservas para los usuarios
    @action(['POST'], detail = False)
    def crear_cliente(self,request):
        #Veriicamos que el motodo sea post
        if (request.method == 'POST'):
            #No cambiaya que siemrpe es cliente (tiene que ser un objeto o no funcionara)
            rol = Rol.objects.get(id=1)
            #Necesitamos lso campos (nombre,correo,foto,contrasena,rol)
            try:

                nombre = request.data['nombre']
                correo = request.data['correo']
                foto = request.data['foto']
                contrasena = request.data['contrasena']


                nuevo_usuario = Usuario.objects.create(
                    nombre=nombre,

                    correo=correo,
                    foto=foto,
                    contrasena=contrasena,
                    rol=rol
                )
                nuevo_usuario.save()
                return Response({f'Nuevo ususario creado {nuevo_usuario.nombre}'},status=status.HTTP_201_CREATED)

            except  Exception as e:
                 return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


    @action(['POST','GET'], detail =  True ,url_path='on-estado')
    def on_estado(self,request,pk):
        usuario=  self.get_object()
        usuario.libre = False

        usuario.save()    
        return Response({"satus": "El doctor esta en vacaciones "})


    @action(['POST','GET'], detail =  True , url_path='off-estado')
    def off_estado(self,request,pk):
        usuario=  self.get_object()

        usuario.libre = True
        usuario.save()

        return Response({"satus": "El doctor NO esta en vacaciones "})