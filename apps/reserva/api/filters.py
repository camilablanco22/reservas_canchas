from django_filters import rest_framework as filters
from apps.reserva.models import Reserva

class ReservaFilter(filters.FilterSet):
    fecha = filters.DateFromToRangeFilter(field_name='fecha')

    class Meta:
        model = Reserva
        fields = ['fecha']
