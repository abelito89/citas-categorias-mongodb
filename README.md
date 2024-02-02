# citas-categorias-mongodb
Ejercicio de introduccion y lectura de citas textuales y sus respectivas categorias en una base de datos de MongoDB
# Generador de Citas

Este proyecto es un generador de citas construido con FastAPI, MongoDB y Jinja2. Permite a los usuarios seleccionar una categoría de cita y genera una cita aleatoria de esa categoría. También permite a los usuarios agregar nuevas citas a la base de datos.

## Estructura del Proyecto

El proyecto consta de tres archivos principales:

- `main.py`: Este es el archivo principal del proyecto. Define la aplicación FastAPI, las rutas y la lógica de la aplicación.

- `index.html`: Este es el archivo de plantilla HTML que se utiliza para generar la interfaz de usuario. Utiliza Jinja2 para la generación dinámica de contenido.

- `style.css`: Este archivo define los estilos CSS que se aplican a la interfaz de usuario.

## Cómo usar

Para usar este proyecto, sigue estos pasos:

1. Clona el repositorio en tu máquina local.
2. Instala las dependencias necesarias (FastAPI, pymongo, pandas, Jinja2).
3. Inicia el servidor de FastAPI con el comando `uvicorn main:app --reload`.
4. Abre un navegador web y navega a `localhost:8000/formulario_inicio` para empezar a usar el generador de citas.
