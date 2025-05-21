from rest_framework import viewsets

from apps.reserva.models import Cancha, Reserva, Turno
from apps.reserva.serializers import CanchaSerializer, ReservaReadSerializer, ReservaSerializer, TurnoSerializer
from apps.usuario.models import Usuario

class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer

class CanchaViewSet(viewsets.ModelViewSet):
    queryset= Cancha.objects.all()
    serializer_class= CanchaSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset= Reserva.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ReservaReadSerializer
        return ReservaSerializer

    def perform_create(self, serializer):
        user = Usuario.objects.first()
        #serializer.save(publicado_por=self.request.user)
        serializer.save(usuario=user)