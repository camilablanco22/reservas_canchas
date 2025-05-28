from decimal import Decimal

import pytz
from rest_framework import serializers
from datetime import datetime
from apps.reserva.models import Cancha, Reserva, Turno
from apps.reserva.api.conversion import convertir_moneda



class CanchaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cancha
        fields= [
            'uuid',
            'numero',
            'superficie',
            'precio_por_hora',
            'activa',
        ]
        read_only_fields = ['uuid']

class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = ['uuid', 'hora_inicio', 'hora_fin']
        read_only_fields = ['uuid']

    def validate(self, data):
        if data['hora_fin']<= data['hora_inicio']:
            raise serializers.ValidationError("La hora de incio no puede ser posterior a la hora de fin")
        return data

class TurnoDisponibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = ['hora_inicio', 'hora_fin']



class ReservaSerializer(serializers.ModelSerializer):
    cancha = serializers.PrimaryKeyRelatedField(queryset=Cancha.objects.all(), many=False)
    usuario = serializers.StringRelatedField(many = False)
    turno = serializers.PrimaryKeyRelatedField(queryset=Turno.objects.all(), many=False)
    class Meta:
        model = Reserva
        fields = [
            'uuid',
            'usuario',
            'fecha',
            'turno',
            'cancha',
            'total',
            'activa'
        ]
        read_only_fields =[
            'uuid','total', 'usuario'
            ]

    def validate(self, data):
        #cancha = data.get('cancha')
        #fecha = data.get('fecha')
        #turno = data.get('turno')
        # DAN ERROR EN PATCH YA QUE AL ENVIARSE LA INFORMACION PARCIAL EN EL BODY NO LA ENCUENTRA

        #SOLUCION: SI NO LO ENCUENTRA BUSQUE EN EL ATRIBUTO DE LA RESERVA Y CAMBIE
        cancha = data.get('cancha', getattr(self.instance, 'cancha'))
        fecha = data.get('fecha', getattr(self.instance, 'fecha'))
        turno = data.get('turno', getattr(self.instance, 'turno'))

        # Si estás actualizando una reserva, excluí esa instancia de la búsqueda
        reservas = Reserva.objects.filter(
            activa=True, #Por si se pidio una reserva, pero posteriormente se dio de baja
            cancha=cancha,
            fecha=fecha,
            turno=turno
        ).exclude(id=self.instance.id if self.instance else None)
        #Si se está modificando una reserva, excluye la reserva que se está modificando

        if reservas.exists():
            raise serializers.ValidationError("La cancha ya está reservada para ese turno.")
        return data

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

    total_usd = serializers.SerializerMethodField()
    class Meta:
        model = Reserva
        fields = [
            'uuid',
            'usuario',
            'fecha',
            'turno',
            'cancha',
            'total',
            'total_usd',
            'activa'
        ]
        read_only_fields = [
            'uuid','total', 'usuario'
        ]

    def get_total_usd (self, obj):
        return convertir_moneda(obj.total, 'USD')

