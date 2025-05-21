import pytz
from rest_framework import serializers
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta

from apps.reserva.models import Cancha, Reserva, Turno


class CanchaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cancha
        fields= [
            'id',
            'numero',
            'superficie',
            'precio_por_hora',
            'activa',
        ]

class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = ['id', 'hora_inicio', 'hora_fin']

    def validate(self, data):
        if data['hora_fin']<= data['hora_inicio']:
            raise serializers.ValidationError("La hora de incio no puede ser posterior a la hora de fin")
        return data


class ReservaSerializer(serializers.ModelSerializer):
    cancha = serializers.PrimaryKeyRelatedField(queryset=Cancha.objects.all(), many=False)
    usuario = serializers.StringRelatedField(many = False)
    turno = serializers.PrimaryKeyRelatedField(queryset=Turno.objects.all(), many=False)
    class Meta:
        model = Reserva
        fields = [
            'id',
            'usuario',
            'fecha',
            'turno',
            'cancha',
            'total',
            'activa'
        ]
        read_only_fields =[
            'total', 'usuario'
            ]

    def validate_fecha(self, value):
        #Verificar que el fecha sea posterior a la fecha actual
        zona_horaria = pytz.timezone("America/Argentina/Buenos_Aires")

        # Obtener la fecha actual en esa zona horaria
        fecha_actual = datetime.now(zona_horaria).date()

        if value < fecha_actual:
            raise serializers.ValidationError("La fecha de la reserva no puede ser anterior a la fecha actual.")
        if value == fecha_actual:
            raise serializers.ValidationError("No se permiten reservas para el mismo día.")
        return value



class ReservaReadSerializer(serializers.ModelSerializer):
    cancha = serializers.StringRelatedField(many=False)
    usuario = serializers.StringRelatedField(many = False)
    turno = serializers.StringRelatedField(many=False)
    class Meta:
        model = Reserva
        fields = [
            'id',
            'usuario',
            'fecha',
            'turno',
            'cancha',
            'total',
            'activa'
        ]
        read_only_fields = [
            'total', 'usuario'
        ]