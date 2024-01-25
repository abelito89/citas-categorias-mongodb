from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pymongo
from pymongo import MongoClient
import pandas as pd

app = FastAPI()
templates = Jinja2Templates(directory='./Templates')
# Crea una conexión al servidor de MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Selecciona la base de datos
db = client["citas"]

# Selecciona la colección
coleccion = db["citas"]

# Busca todos los documentos en la colección
query = coleccion.find()

df = pd.DataFrame(query).drop('_id', axis=1)
app = FastAPI()
templates = Jinja2Templates('./Templates')

@app.get('/formulario_inicio', response_class=HTMLResponse)
def leer_formulario(peticion:Request):
    return templates.TemplateResponse('index.html',{'request':peticion})

@app.post('/enviar_categoria')
def enviar_categoria(peticion:Request, categoria:str=Form(...)):
    try:
        if categoria == '-':
            return f'Seleccione una categoria'
        elif categoria not in df['categoria'].values:
            return f'La categoria {categoria} no existe'
        df_filtrado = df[df['categoria'] == categoria]
        serie_aleatoria = df_filtrado.sample(n=1).iloc[0]
        cita_devuelta = serie_aleatoria['cita']
        return templates.TemplateResponse('index.html',{'request':peticion, 'cita_devuelta':cita_devuelta})
    except Exception as e:
        return f'Error procesando el archivo{e}'