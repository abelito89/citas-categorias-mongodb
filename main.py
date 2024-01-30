from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, Response
from fastapi.templating import Jinja2Templates
import pymongo
from pymongo import MongoClient
import pandas as pd
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
app.add_middleware(SessionMiddleware,secret_key="Abelito89*")
templates = Jinja2Templates(directory='./Templates')
# Crea una conexión al servidor de MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Selecciona la base de datos
db = client["citas"]

# Selecciona la colección
coleccion = db["citas"]

@app.get('/formulario_inicio', response_class=HTMLResponse)
def leer_formulario(peticion:Request):
    #global df, lista_categorias, categoria_seleccionada
    
    query = coleccion.find()
    df = pd.DataFrame(query).drop('_id', axis=1)
    lista_categorias = df['categoria'].unique()
    categoria_seleccionada = peticion.session.get('categoria_seleccionada','-')
    peticion.session['categoria_seleccionada']=categoria_seleccionada
    
    return templates.TemplateResponse('index.html',{'request':peticion, 'lista_categorias':lista_categorias, 'categoria_seleccionada':categoria_seleccionada})

@app.post('/enviar_categoria')
def enviar_categoria(peticion:Request, categoria_seleccionada:str=Form(...)):
    try:
        query = coleccion.find()
        df = pd.DataFrame(query).drop('_id', axis=1)
        lista_categorias = df['categoria'].unique()
        if categoria_seleccionada == '-':
            return templates.TemplateResponse('index.html',{'request':peticion, 'cita_devuelta':'Seleccione una categoría válida', 'lista_categorias':lista_categorias})
        elif categoria_seleccionada not in df['categoria'].values:
            return f'La categoria {categoria_seleccionada} no existe'
        
        df_filtrado = df[df['categoria'] == categoria_seleccionada]
        serie_aleatoria = df_filtrado.sample(n=1).iloc[0]
        cita_devuelta = serie_aleatoria['cita']
        return templates.TemplateResponse('index.html',{'request':peticion, 'cita_devuelta':cita_devuelta, 'categoria':categoria_seleccionada, 'lista_categorias':lista_categorias})
    except Exception as e:
        return f'Error procesando el archivo {e}'
    
@app.post('/nuevos_datos')
def nueva_cita(peticion:Request, cita:str=Form(...), categoria:str=Form(...)):
    try:
        nuevo = coleccion.insert_one({'cita':cita, 'categoria':categoria})
        peticion.session['categoria_seleccionada'] = '-'
        return Response(status_code=303, headers={'Location': '/formulario_inicio'})
    except Exception as e:
        return {"error":str(e)}
