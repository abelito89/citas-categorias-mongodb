from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()
templates = Jinja2Templates(directory='./Templates')
lista_comentarios_usuarios=[]

@app.get('/formulario', response_class=HTMLResponse)
def mostrar_comentarios(peticion:Request):
    return templates.TemplateResponse('index.html',{'request':peticion})

@app.post('/enviar_comentario')
def comentar(peticion:Request, comentario:str=Form(...)):
    lista_comentarios_usuarios.append(comentario)
    return templates.TemplateResponse('index.html',{'request':peticion, 'lista_comentarios_usuarios':lista_comentarios_usuarios})

@app.post('/resetear')
def resetear_comentarios(peticion:Request):
    lista_comentarios_usuarios.clear()
    return templates.TemplateResponse('index.html',{'request':peticion})
