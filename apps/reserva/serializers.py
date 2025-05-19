from rest_framework import serializers
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta

from apps.reserva.models import Cancha, Reserva


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


class ReservaSerializer(serializers.ModelSerializer):
    cancha = serializers.PrimaryKeyRelatedField(queryset=Cancha.objects.all(), many=False)
    usuario = serializers.StringRelatedField(many = False)
    class Meta:
        model = Reserva
        fields = [
            'id',
            'fecha',
            'hora_inicio',
            'hora_fin',
            'activa',
            'cancha',
            'usuario', #
            'precio_total'
        ]
        read_only_fields =[
            'precio_total'
            ]

    def validate_fecha(self, value):
        #Verificar que el fecha sea posterior a la fecha actual
        fecha_actual = datetime.now(timezone.utc).date()

        if value < fecha_actual:
            raise serializers.ValidationError("La fecha de la reserva no puede ser anterior a la fecha actual.")
        return value

    def validate(self, data):
        # Validar que la hora de fin sea posterior a la hora de inicio
        if data['hora_fin'] <= data['hora_inicio']:
            raise serializers.ValidationError("La hora de fin debe ser posterior a la hora de inicio.")

        #Validar solapamiento de reservas en la misma cancha
        reservas_existentes = Reserva.objects.filter(
            fecha=data['fecha'],
            cancha=data['cancha'],
            activa=True
        )

        for reserva in reservas_existentes:
            inicio_existente = reserva.hora_inicio
            fin_existente = reserva.hora_fin
            nuevo_inicio = data['hora_inicio']
            nuevo_fin = data['hora_fin']

            if not (nuevo_fin <= inicio_existente or nuevo_inicio >= fin_existente):
                raise serializers.ValidationError("Ya existe una reserva en ese horario para esta cancha.")

        return data




class ReservaReadSerializer(serializers.ModelSerializer):
    cancha = serializers.StringRelatedField(many=False)
    usuario = serializers.StringRelatedField(many = False)
    class Meta:
        model = Reserva
        fields = [
            'id',
            'fecha',
            'hora_inicio',
            'hora_fin',
            'activa',
            'cancha',
            'usuario', #
            'precio_total'
        ]
        read_only_fields =[
            'precio_total'
            ]