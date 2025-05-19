from rest_framework import routers

from apps.reserva.api import CanchaViewSet, ReservaViewSet

#Initializarel router de DRF solo unavez
router = routers.DefaultRouter()
# Registrar un ViewSet
router.register(prefix='cancha', viewset=CanchaViewSet)
router.register(prefix='reserva', viewset=ReservaViewSet)