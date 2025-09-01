from rest_framework.viewsets import ModelViewSet
from .models import EstadoReserva,Reserva
from rest_framework import status
from .serializers import EstadoReservaSerializer,ReservaSerializer
from mesa.models import Mesa

from usuario.models import Usuario,Rol
from rest_framework.response import Response
from rest_framework.decorators import action
from datetime import datetime




class ReservaViewSet(ModelViewSet):    

    #Agregamos el serializer que necesita para traducir de SQL A JSON y viceversa
    serializer_class = ReservaSerializer
    #Agregamos el queryset, el cual es el Modelo Usuario (que contiene todos los registros)
    
    #Y solicitamos todos los registros, se actualiza cuando se actualizen los registros en la Base de datos

    queryset = Reserva.objects.all()
    #FUNCIONES DEL VIEWSET AQUI....
    #FUNCIONES DEL CLIENTE

    @action(methods=["POST"],detail = False)
    def Reservar(self,request):
        #Usamos el metodo post como respuesta
            #Tomamos los datos de la reserva
            #Nos llega en string asi que usamos datetime para convertirlos al formato
            # que nos permite operarlos mas comodamente
            fecha_inicio = datetime.fromisoformat(request.data['fecha_inicio'])  
            fecha_final = datetime.fromisoformat(request.data['fecha_final'])


            #Agregamos estas secciones de verifiacacines
            #las cuales objtenemos los objetso delos modelos (esatdo,mesa y usuario)
            # y determianmos si es valida o no
            #estado id = 1 DISPONIBLE
            #estado id = 2 RESERVADO
            #estado id = 3 USADO




            try:
                estado = EstadoReserva.objects.get(id=1)
            except Exception as e:
                return Response({"error en encontrar el estado en el modelo": str(e)})
            #Verificammos que exista la mesa
            try:
                mesa = Mesa.objects.get(numero=request.data['mesa'])
                print(request.data['mesa'])
            except Exception as e:
                return Response({"Error al muscar la mesa en el modelo ": str(e)})

            #Verificamso que exista el perfil, y que sea de un cliente
            try:
                #Consultamos el usuario que tiene el correo que envio desde el html
                usuario = Usuario.objects.get(correo=request.data['usuario'])
                #Rol esperado(Cliente) lo sacamos del usuario y miramos su rol
                
                rol_valido = Rol.objects.get(id=1)


                if (usuario.rol == rol_valido):
                    print("El rol es el correcto")
                    
                else:
                    return Response({"El usuario no correponde al rol de cliente"},status=status.HTTP_404_NOT_FOUND)

            except Exception as e:
                return Response({"error al buscar el usuario en el modelo": str(e)})


            #Si no se rompe en ninguna de las anteriores partes 

            # ahora consultamos LA RESERVA CON LOS DATOS BRINDADOS EN LAS HORAS,ESTADO DISPONIBLE
            # Y MESA, usamos el filter para que o se rompa si no encuentra resultados
            reserva = Reserva.objects.filter(mesa=mesa,

            fecha_inicio=fecha_inicio,fecha_final=fecha_final,estado=estado).first()

            # #Verificamos si existe la reservada cone esta      funcion
            if reserva:

                # Si existe Le cambiamos el estado a "Reservado"  y le asignamos el usuario que la solicito
                #Y le pasamos los datosque obtuvimos arriba de los modelos
                #Creamos el nuevoe estado y lo actualizamos(1 es disponible 2 es reseravdo)
                estado_nuevo = EstadoReserva.objects.get(id=2)

                reserva.estado = estado_nuevo
                reserva.usuario = usuario
                # y guardamos el cambio en los modelos con .save() en la abse de datos
                reserva.save()
                #Retornamos un estado afirmativo para que confirme que se reservo
                return Response("Reserav realizada con exito! ",status=status.HTTP_200_OK)
            else:
                # Si no existe retorna un status error con un HTTP_404_NOT_FOUND
                return Response("No se encontro una reserva con estas caracteristicas",status=status.HTTP_404_NOT_FOUND)



    #METODO PARA DEVOLVER LAS RESERVAS POR MESAS (FUNCIONA)
    @action(methods=['GET'] ,detail = False)
    def Reservas_Disponibles(self,request):

        reservas = Reserva.objects.all()
        mesas = Mesa.objects.all()
        reservas_por_mesa = []
        #Ciclo para recorrer las mesas existentes
        #Variable para traer el objeto Estado con el valor disponible
        # (para compararloc on el de reservas)
        estado = EstadoReserva.objects.get(id=1,nombre='Disponible')
        for mesa in mesas:
            
            
            #Variable para almacenar las reservas de esa mesa
            reservas_mesa = {
                "mesa": mesa.numero,

                "reservas" : []
            }
            #Ciclo querecorre las reservas (Por cada mesa, busca las reservas que 
            # pertenescan a la mesa y su estado se igual a disponible)
            for reserva in reservas:
                #Verificamso (Por cada mesa, busca las reservas que 
                # pertenescan a la mesa y su estado se igual a disponible)
                if(reserva.estado == estado and reserva.mesa == mesa):
                    #Serializamos la reserva(pasamos a json) para 

                    reserva = ReservaSerializer(reserva).data
                    #Añadimos a la lista por mesa
                    reservas_mesa['reservas'].append(reserva)  
            #Al termianr el ciclo agrega la lista resreavs_por_mesa
            reservas_por_mesa.append(reservas_mesa)
        return Response(reservas_por_mesa)


        

#Viewset de Estado de reseravs
class EstadoReservaViewSet(ModelViewSet):
    #Serializer
    serializer_class = EstadoReservaSerializer


    #Queryset
    queryset = EstadoReserva.objects.all()
    #FUNCIONES DEL VIEWSET AQUI....