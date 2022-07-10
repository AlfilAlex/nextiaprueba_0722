# Prueba técnica desarrollador Backend

## Descripción

Respo con el código de la prueba técnia de desarrollador backend con Python para Nextia en la que se crearon diferentes EP para registro, login de usuarios y la creación de objetos denominados 'bienes'. Para la seguridad se implementó JWT y se protegieron las rutas mediante este protocolo.

Utilizar el requirement.txt para generar una copia en environment.

## Objetivo

Con la siguiente prueba técnica se pretende obtener una visión más certera del conocimiento
de quien aplica a la vacante de desarrollador Backend.

## Herramientas a implementar.

-   Django Rest Framework
-   Postgres
-   Pandas
-   Git
-   Repositorio online. (Github, gitlab, etc)

## Justificación de los puntos a desarrollar

1. Configuración del proyecto
   Creación de archivo .env para almacenar variables de entorno y archivo .gitignore para evitar compartir información privada.
   Creación del archivo requirements.txt para duplicar el entorno virtual.

2. Crear un Modelo “Base” del cual heredarán los demás modelos.
   Modelo base en app_prueba/app/models/base_model.py.
   Se implementó la propiedad **abstract**=True, que permite generar un modelo sin que SQLAlchemy genere una tabla para este. Con lo cual es posible hererdad sus propiedad sin utilizar un mapping.

3. Generar un modelo para usuarios (que herede de BaseModel).
   Se implementó el modelo users en: app_prueba/app/models/user.py.
   Se heredó de ModeloBase las propiedad pertienentes.

Se declaró como _unique_ la propiedad usuario.

4. Autenticación de usuarios bajo el
   estándar JWT.
   Se generó una SECRET_KEY utilizada para la encriptación de los datos y se obtuvo un decorador que permite realizar la autenticación de los usuarios.
   Se considera buena idea implementar las siguientes caracteristicas:

-   Una propiedad exp del token y la renovación de este cada inicio de sesión.

5. Crear un modelo llamado Bienes (que herede de BaseModel).
   Se implementó el modelo users en: app_prueba/app/models/bienes.py.
   Se heredó de ModeloBase las propiedad pertienentes.

6. Registro de usuarios y carga de los datos del csv a la base de datos.
   Para implementar estas funcionalidades se optó por generar EP, que a su vez pueden ser útiles para automatizar diferentes tareas.

-   Un EP para el registro de usuarios a través de un formulario
-   Un EP para que usuarios registrados puedan subir archivos csv para registrar sus bienes.
    Esta ruta está protegida con JWT.

7. Crear endpoints CRUD para el modelo Bienes protegidos con JWT.

-   EP Create: Creación de bienes a partir de datos de un formulario
-   EP Read: Obtención de beienes a partir de ids de bienes
-   EP Update: Modificación de bienes a partir de un id y los nuevos valores.
-   EP Delete: Eliminación de un bien a partir de su id.

8. Crear un endpoint para solicitar información de Bienes a través de múltiples id’s.

## Puntos a desarrollar

1. Crear proyecto y configuración.
2. Crear un Modelo “Base” del cual heredarán los demás modelos que creemos en nuestro
   proyecto. Este Modelo “Base” contendrá los siguientes campos
   a. id = primary key
   b. created_at = Tipo fecha, que se guarde automáticamente al crear un registro
   c. updated_at = Tipo fecha, este se actualizará siempre que se actualice un
   registro.
3. Generar un modelo para usuarios (que herede de BaseModel), NOTA. este modelo se
   utilizará también para el proceso de autenticación, los datos que almacenará dicho
   modelo son los siguientes.
   a. Nombre
   b. Usuario
   c. Contraseña (Guardarla encriptada)

4. Realizar endpoints y lógica para la autenticación de usuarios, se tendrá que hacer bajo el
   estándar JWT.
   a. Endpoint para generar JWT en base a usuario y contraseña.
   b. Endpoint para crear usuario y crear JWT al momento de que se registre el
   usuario.
5. Crear un modelo llamado Bienes (que herede de BaseModel). Los datos que almacenará
   son los siguientes.
   a. articulo = Tipo string, max 255
   b. descripcion = Tipo string, max 255
   c. usuario_id = Relación a modelo Usuario.
6. Crear un script el cual registre un usuario en la base de datos (Esto por que el Modelo
   Bien requiere de un usuario existente), seguido de esto se te compartió un archivo csv
   con ayuda de la librería pandas importar toda la información de ese archivo a la base de
   datos al modelo Bienes, el id del usuario registrado previamente se tendrá que
   almacenar en cada registro.
7. Crear endpoints CRUD para el modelo Bienes. Es importante que al regresar la
   información siempre regrese el objeto usuario. Importante: Todos los endpoints tienen
   que tener seguridad JWT.
8. Crear un endpoint especial para Bienes al cual se le puedan enviar múltiples id’s y este
   me regrese un array de los registros solicitados.
