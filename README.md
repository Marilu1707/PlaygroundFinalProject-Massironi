# Coderhouse-56065-Django

## Entornos virtuales

Un entorno virtual en Python es una herramienta 
que te permite crear un espacio aislado donde puedes instalar 
y manejar las dependencias (bibliotecas y versiones de Python) 
específicas para un proyecto en particular, sin afectar al sistema global

- `pip list`: Muestra las bibliotecas instaladas en el entorno virtual o global

¿Cómo crear un entorno virtual? (entorno aislado del global)

- `python -m venv .venv` (Windows)
- `python3 -m venv .venv` (Linux o Mac)

¿Cómo activar el entorno virtual?
- `.\.venv\Scripts\activate`  (Windows Powershell)
- `source .venv/bin/activate` (Linux o Mac)

¿Cómo crear requirements.txt?
- `pip freeze >> requirements.txt`

¿Cómo instalar paquetes desde requirements.txt?
- `pip install -r requirements.txt`

## Instalación Django

- `pip install django`

## Crear un proyecto
    
1. Crear una carpeta para el proyecto en la raiz:
    - `md project`

2. Acceder a la carpeta `project`
    - `cd project`

3. Crear las carpetas y archivos necesarios
    - `django-admin startproject config .`

4. Ejecutar el servidor:
    - `python manage.py runserver`

## Crear una aplicación:

1. Estar ubicado dentro de `project` pero fuera de `config`
    - `cd ..`
    - `ls`

2. Crear una carpeta para que contenga las aplicaciones
    - `md apps`

3. Acceder a la carpeta `apps`
    - `cd apps`

4. Crear la aplicación Django con el nombre que desee
    - `django-admin startapp core`

5. Agregar el nombre de la app en lista `config.settings.INSTALLED_APPS`

6. Agregar el siguiente código a `config.settigs`

    ```py
    import sys

    sys.path.append(str(BASE_DIR / "apps"))
    ```

## Establecer `config.settings.SECRET_KEY`

```py
from django.core.management.utils import get_random_secret_key

SECRET_KEY = get_random_secret_key()
```

## Crear base de datos

Crear archivos Python pre-SQL:

- `python manage.py makemigrations`

Crear SQL y modificar base de datos:

- `python manage.py migrate`

## Crear superusuario

- `python manage.py createsuperuser`
