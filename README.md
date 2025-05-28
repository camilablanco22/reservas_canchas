# Proyecto: reservas_canchas

## Descripción general

### Introducción

El sistema tiene como objetivo gestionar las reservas de canchas de pádel en un club deportivo.  
Los usuarios podrán:

- Consultar la disponibilidad de turnos (general o por cancha).
- Realizar, modificar o cancelar reservas.
- Visualizar su historial de reservas.

Además, los empleados del club podrán:

- Agregar o modificar canchas.
- Consultar reservas por día, por período o por cancha.
- Visualizar únicamente las reservas activas.

---

### Objetivos

- Permitir a los usuarios consultar horarios disponibles (por cancha o general) en una fecha dada.
- Habilitar la reserva de canchas disponibles.
- Calcular el costo de la reserva y mostrar su valor equivalente en dólares.
- Permitir a los administradores crear y gestionar las canchas.
- Definir los turnos de las canchas según lo disponga el administrador.

---

## Modelos principales

### Cancha

- `numero`: número identificador de la cancha.
- `tipo_superficie`: cemento, sintético.
- `precio_por_hora`: valor monetario por hora de uso.
- `estado`: activa/inactiva.

### Turno

- `hora_inicio`: hora de comienzo del turno.
- `hora_fin`: hora de finalización del turno.

### Reserva

- `usuario`: persona que realiza la reserva.
- `cancha`: cancha seleccionada.
- `fecha`: día de la reserva.
- `turno`: franja horaria reservada.
- `estado`: activa o cancelada.
- `total`: monto final de la reserva.

---

## Requisitos del laboratorio

- Elegir un dominio de aplicación validado por el profesor (reservas de canchas).
- Redactar un documento con los requisitos del desarrollo de la API.
- Definir al menos tres modelos relacionados entre sí.
- Implementar una API REST con operaciones CRUD para los modelos definidos.
- Desarrollar al menos un endpoint con lógica adicional (ej. cálculo de valor en USD).
- Agregar validaciones avanzadas en los serializadores.
- Incluir métodos adicionales en modelos o serializadores para cálculos específicos (ej. total de la reserva).
- Utilizar vistas del DRF (`APIView`, `ViewSet`, `GenericAPIView`, etc.).
- Implementar autenticación con JWT y permisos con `DjangoModelPermission`.
- Agregar filtros y paginación en listados.
- Consumir una API externa para conversión a dólares (https://dolarapi.com/v1/dolares/blue).
- Mantener una estructura de proyecto clara y ordenada.
- Documentar todos los endpoints en Postman.
- Subir el código a un repositorio público con documentación de uso.


