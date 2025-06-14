# Generated by Django 5.2 on 2025-05-26 23:59

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('numero', models.PositiveIntegerField(unique=True)),
                ('superficie', models.CharField(choices=[('CEMENTO', 'CEMENTO'), ('SINTETICO', 'SINTETICO')])),
                ('precio_por_hora', models.DecimalField(decimal_places=2, max_digits=10)),
                ('activa', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('fecha', models.DateField()),
                ('activa', models.BooleanField(default=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('cancha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='reserva.cancha')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('turno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reserva.turno')),
            ],
        ),
    ]
