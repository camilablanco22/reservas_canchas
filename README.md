# reservas_canchas.
## Descripción general del proyecto.
### Introducción.
El sistema tiene como objetivo permitir la gestión de reservas de canchas de pádel en un club deportivo. Los usuarios podrán consultar la disponibilidad de turnos en general o especificamente de una cancha, hacer reservas, modificar o cancelar sus turnos, y visualizar el historial de reservas realizadas. Además, debe permitir a los usuarios de empleados agregar o modificar canchas, visualizar las reservas de un día o de un período determinado, las reservas de una cancha específica y reservas unicamente activas.
### Objetivos.
- Permitir que los usuarios consulten los horarios disponibles de todas las canchas o de una cancha específica para una fecha dada. 
-	Permitir la reserva de canchas disponibles.
-	Calcular el costo de la reserva y permitir consultar su valor en dólares.
-	Permitir a los administradores crear y gestionar las canchas del club.
-	Permitir a los administradores definir los turnos de las canchas como crean conveniente.

## Modelos principales.
### Cancha:
- Número de cancha.
- Tipo de superficie (cemento, sintético).
- Precio por hora.
- Estado de la cancha (activa).
### Turno:
- Hora de inicio.
- Hora de fin.
### Reserva:
- Usuario que realiza la reserva.
- Cancha.
- Fecha.
- Turno.
- Estado de la reserva (activa).
- Total.
## Requisitos del laboratorio
- Elegir un dominio de aplicación (Ejemplo: gestión de biblioteca, reservas de hoteles, pedidos en restaurantes, etc.) y validarlo con el profesor de la materia. 
- Redactar un documento con los requisitos de desarrollo del API en base al caso de estudio seleccionado. 
- Definir los modelos principales que formarán parte del sistema (como mínimo se piden tres modelos relacionados entre sí). 
- Implementar una API REST que permita realizar operaciones CRUD sobre los modelos definidos. 
- Desarrollar al menos un endpoint que realice una operación más allá de un CRUD básico, por ejemplo: “permitir realizar una oferta sobre un artículo en una subasta”. 
- Implementar validaciones avanzadas en serializadores para garantizar la coherencia e integridad de los datos, más allá de comprobaciones básicas como la presencia de un valor en un campo. 
- Implementar métodos adicionales en los modelos o serializadores para cálculos específicos siempre que sea adecuado para el caso de estudio (Ejemplo: cálculo de 
total en una orden, validación de stock en una compra, etc.).
- Utilizar una o varias de las vistas de Django Rest Framework (APIView, ViewSet, Generic Views, etc.) para desarrollar el API, según las necesidades del caso de 
estudio. 
- Implementar JWT como mecanismo de autenticación al API y el permiso DjangoModelPermission para la autorización, para proteger endpoints sensibles y garantizar un acceso seguro. 
- Implementar filtros y paginación en listados de objetos. 
- Implementar alguna funcionalidad donde se deba consumir un API externa. Por ejemplo: dado un monto en moneda Pesos Argentinos, calcular su equivalente en 
Dolares, obteniendo información  en línea desde API de https://dolarapi.com/v1/dolares/blue.
- Estructurar el proyecto, archivos, urls de acuerdo a las buenas practicas sugeridas. 
- Documentar el proyecto mediante Postman, registrando cada endpoint que proporciona el API. 
- Subir el código a un repositorio público y documentar los endpoints disponibles y su uso. 
