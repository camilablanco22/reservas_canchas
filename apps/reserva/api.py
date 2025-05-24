from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.reserva.filters import ReservaFilter
from apps.reserva.models import Cancha, Reserva, Turno
from apps.reserva.serializers import CanchaSerializer, ReservaReadSerializer, ReservaSerializer, TurnoSerializer, \
    TurnoDisponibleSerializer
from apps.usuario.models import Usuario

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
        user = Usuario.objects.first()
        #serializer.save(usuario=self.request.user)
        serializer.save(usuario=user)


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
