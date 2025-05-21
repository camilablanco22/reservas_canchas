from rest_framework import routers

from apps.reserva.api import CanchaViewSet, ReservaViewSet, TurnoViewSet

#Inicializar el router de DRF solo una vez
router = routers.DefaultRouter()
# Registrar un ViewSet
router.register(prefix='cancha', viewset=CanchaViewSet)
router.register(prefix='reserva', viewset=ReservaViewSet)
router.register(prefix='turno', viewset=TurnoViewSet)