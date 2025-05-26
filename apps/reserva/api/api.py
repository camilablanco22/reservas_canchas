from datetime import datetime

import pytz
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.reserva.api.filters import ReservaFilter
from apps.reserva.models import Cancha, Reserva, Turno
from apps.reserva.api.serializers import CanchaSerializer, ReservaReadSerializer, ReservaSerializer, TurnoSerializer, \
    TurnoDisponibleSerializer


class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer

class CanchaViewSet(viewsets.ModelViewSet):
    queryset= Cancha.objects.all()
    serializer_class= CanchaSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset= Reserva.objects.all()
    filterset_fields = ['fecha', 'cancha', 'estado']
    filterset_class = ReservaFilter

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ReservaReadSerializer
        return ReservaSerializer

    def perform_create(self, serializer):
        #user = Usuario.objects.first()
        serializer.save(usuario=self.request.user)
        #serializer.save(usuario=user)

    #Controla que un usuario normal solo pueda las reservas que el ha realizado
    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Reserva.objects.all()
        return Reserva.objects.filter(usuario=user)

    #Control que no se pueda entrar a la url de una reserva ajena
    def get_object(self):
        obj = super().get_object()
        if not (self.request.user.is_staff or self.request.user.is_superuser):
            if obj.usuario != self.request.user:
                raise PermissionDenied("No tenés permiso para ver esta reserva.")
        return obj
    #PARA PUT
    def update(self, request, *args, **kwargs):
        reserva = self.get_object()

        # Control de usuario
        if not (request.user.is_staff or reserva.usuario == request.user):
            raise PermissionDenied("No podés modificar esta reserva.")

        #Validar que la reserva no sea para hoy o antes
        if not request.user.is_staff:
            hoy = datetime.now(pytz.timezone("America/Argentina/Buenos_Aires")).date()
            if reserva.fecha <= hoy:
                raise ValidationError("No se puede modificar una reserva para el mismo día o para fechas anteriores.")

        return super().update(request, *args, **kwargs)

    #PARA PATCH
    def partial_update(self, request, *args, **kwargs):
        reserva = self.get_object()

        #Control de usuario
        if not (request.user.is_staff or reserva.usuario == request.user):
            raise PermissionDenied("No podés modificar esta reserva.")

        #Validar que la reserva no sea para hoy o antes
        if not request.user.is_staff:
            hoy = datetime.now(pytz.timezone("America/Argentina/Buenos_Aires")).date()
            if reserva.fecha <= hoy:
                raise ValidationError("No se puede modificar una reserva para el mismo día o para fechas anteriores.")

        return super().partial_update(request, *args, **kwargs)


class TurnosDisponiblesPorCanchaView(APIView):
    def get(self, request):
        fecha = request.query_params.get('fecha')
        if not fecha:
            return Response({"error": "Se requiere el parámetro 'fecha' (YYYY-MM-DD)."}, status=400)

        resultado = []

        for cancha in Cancha.objects.all():
            turnos_ocupados = Reserva.objects.filter(
                fecha=fecha,
                cancha=cancha
            ).values_list('turno_id', flat=True)

            turnos_disponibles = Turno.objects.exclude(id__in=turnos_ocupados)
            serializer = TurnoDisponibleSerializer(turnos_disponibles, many=True)

            resultado.append({
                "cancha_numero": cancha.numero,
                "cancha_superficie":cancha.superficie,
                "turnos_disponibles": serializer.data
            })

        return Response(resultado)
