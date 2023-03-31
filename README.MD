# Credit-Backend

###### _Created on: 31/03/2023_

### Ejecución del proyecto tu Crédito

---

#### **Pre-requisitos**

- Tener instalado Python 3. (**Clic para descargar [Python](https://www.python.org/downloads/)** )
- Instalar el entorno virtual para el control de paquetes de un proyecto usando el siguiente comando:

  ```
      pip install virtualenv
  ```

> El gestor de paquetes ya está en Windows, sin embargo en Linux es necesario descargarlo.  
> Al hacer clic en el siguiente enlace se puede descargar [PIP](https://packaging.python.org/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers)

- Descarga de repositorios:
  credit-backend (backend)

#### **Paso 1. Creación y activación del entorno virtual**

---

**1.- Crear el entorno virtual**

Acceder a la terminal / consola de comando y utilizar:

        virtualenv -p python3 venv

> Al final del comando puede escribirse un nombre cualquiera, en este caso se utilizó el nombre venv

Con este comando se crea una carpeta para el entorno virtual que no está incluida en el proyecto con el nombre asignado, **_venv_** en este caso, y **de esta forma queda establecido el entorno virtual**.

**2.- Activar el entorno virtual**

Acceder a la carpeta, con el nombre asignado (**_venv_**), desde la terminal / consola de comandos y utilizar:

```Bash
Source bin/activate  (Linux)
Scripts/activate  (Windows)
```

> Para salir usar el comando deactivate dentro de la carpeta (**_venv_**)

**3.- Instalar las librerías dentro del entorno virtual**

Ejecutar el siguiente comando:

        pip install -r requirements.txt

Con este comando se instalan todas las librerías del repositorio dentro del entorno virtual para ejecutar el proyecto.

### **Paso 2. Creación de una base de datos**

---

_Crear una base de datos local en PostgreSQL._

> Debe coincidir la información de la base de datos y usuario de **PostgreSQL** con el archivo .env

### **Paso 3. Migración de la Data**

---

1.- Crear un archivo .env dentro de la raíz del proyecto y organizarlo dentro de la carpeta src.

2.- Abrir el archivo .env, copiar y pegar los siguientes datos:

    DEBUG=true
    URL=http://127.0.0.1:8000
    FRONT_URL=http://127.0.0.1:3000/
    SECRETKEY=django-secret-key
    DB_HOST=db
    DB_PORT=5432
    DB_NAME=app
    DB_USER=postgres
    DB_PASSWORD=supersecretpassword
    POSTGRES_DB=app
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=supersecretpassword
    EMAIL_TLS=False
    EMAIL_SSL=True
    EMAIL_PORT_USE=587
    EMAIL_USER=email@gmail.com
    EMAIL_PASSWORD=email123
    BROKER_TRANSPORT=redis://127.0.0.1:6379/0
    BROKER_HOST=127.0.0.1
    BROKER_PORT=6379
    BROKER_VHOST=0
    BROKER_PASSWORD=redis
    CELERY_RESULT_BACKEND=redis://redis:6379
    CELERY_BROKER_URL =redis://redis:6379
    CELERY_REDIS_HOST=127.0.0.1
    CELERY_REDIS_PORT=6379
    CELERY_REDIS_DB=0
    REDIS_DB=0
    PAGE_SIZE=20


3.- Modificar los datos necesarios. La información más importante que debe ser modificada para ejecutar el proyecto es la mencionada debajo:

    DEBUG=True
    DBUSER=example
    DBNAME=example
    DBPASSWORD=example
    DBHOST=127.0.0.1
    DBPORT=5432
    URL=http://127.0.0.1:8000/

### **Paso 4. Creación de superuser en Django**

---

Para acceder al admin de Django se debe crear un superuser (o superusuario) con el comando:

        python manage.py createsuperuser

### **Paso 5. Activación del server**

---

1.- Encender el server.

2.- Iniciar el server con el siguiente comando:

        python manage.py runserver

> Usar el url que proporciona el server y agregarle **/admin** al final para ingresar a credit-backend como admin. Debajo se muestra un ejemplo.

    http://127.0.0.1:8000/admin


#### **Creación y activación del entorno via docker**

1.- instalar docker [DOCKER](https://docs.docker.com/docker-for-windows/install/)

2.- ejecutar el comando:

        docker-compose build

3.- ejecutar el comando

        docker-compose up

4.- ejecutar las migracion

        docker-compose run --rm app python manage.py migrate

5.- crear un superusuario

        docker-compose run --rm app python manage.py createsuperuser 


# NOTA

