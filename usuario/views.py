from .serializers import UsuarioSerializer, RolSerializer
from .models import Usuario,Rol
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.generics import RetrieveUpdateDestroyAPIView


class ListaUsuarios(APIView):
    allowed_methods = ['GET','POST']
    
    def get(self,request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)

        return Response(serializer.data)

    def post(self,request):
        serializer = UsuarioSerializer(data = request.data)
        is_valid = serializer.is_valid(raise_exception=True)

        if (is_valid):
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)




class ListRoles(APIView):
    """

    Nos permite llamar la lista de roles existentes para lso usuarios
    """
    allowed_methods= ['GET']
    
    def get(self,request):
        """ obtenerlo"""
        roles = Rol.objects.all()

        serializer = RolSerializer(roles, many=True)
        return Response(serializer.data)






class DetalleUsuario(RetrieveUpdateDestroyAPIView):

    
    """
    Esta funcion nos muestra el detalle del ususario, nos permite:
    ['GET','PUT','DELETE']
    """
    
    allowed_methods = ['GET','PUT','DELETE']
    serializer_class = UsuarioSerializer

    queryset = Usuario.objects.all()

#Metodos anteriores con funciones

""" @api_view(['GET','POST'])
def list_usuarios(request):
    
    if (request.method == 'GET'):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)
    if (request.method == 'POST'):

        serializer = UsuarioSerializer(data = request.data)
        is_valid = serializer.is_valid(raise_exception=True)
        if (is_valid):
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)
  """
""" @api_view(['GET'])
def list_roles(request):

    if(request.method == 'GET'):
        roles = Rol.objects.all()
        serializer = RolSerializer(roles, many=True)

        return Response(serializer.data) """

"""
@api_view(['GET','POST','DELETE'])
def detalle_usuario(request,pk):

    try:
        usuario = Usuario.objects.get(id = pk)
    except Usuario.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = UsuarioSerializer(usuario, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    if request.method == 'DELETE':
        usuario.delete()
        return Response(status =  status.HTTP_204_NO_CONTENT)
    """
