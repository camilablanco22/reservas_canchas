from rest_framework import viewsets

from apps.reserva.models import Cancha, Reserva
from apps.reserva.serializers import CanchaSerializer, ReservaReadSerializer, ReservaSerializer
from apps.usuario.models import Usuario


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