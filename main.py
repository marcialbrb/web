#CREADO POR MARCIAL BARBOZA

from flask import Flask, render_template,url_for,redirect, request, flash
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap
from config import DevelopmentConfig

from decouple import config as config_decouple

import forms #importando mi archivo forms.py
import config

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object(DevelopmentConfig)
    
enviroment = config['development']
if config_decouple('PRODUCTION', default=False):
        enviroment = config['production']

app = create_app(enviroment)

#PROTECCIÓN DE SEGURIDAD CSRF
csrf = CSRFProtect()

#ROUTES - NAVPAGES
@app.route("/")
@app.route("/home")
def index():
    titulo= "Marcial Barboza - Website"
    return render_template("index.html", tituloHTML= titulo)

@app.route("/projects")
def projects():
    titulo= "Marcial Barboza - Projects"
    return render_template("projects.html", tituloHTML= titulo)

@app.route("/gallery")
def gallery():
    titulo= "Marcial Barboza - Gallery"
    return render_template("gallery.html", tituloHTML= titulo)

@app.route("/gallery/art")
def art():
    titulo= "Marcial Barboza - Art"
    return render_template("art.html", tituloHTML= titulo)

@app.route("/gallery/photography")
def photography():

    titulo= "Marcial Barboza - Photography"
    return render_template("photo.html", tituloHTML= titulo)

@app.route("/about")
def about():
    titulo= "Marcial Barboza - About me"
    return render_template("about.html", tituloHTML= titulo)

@app.route("/contact", methods=['GET','POST'])
def contact():
    correo_send = forms.correo(request.form) #importo la clase form de mi archivo forms.py
    
    if request.method == 'POST' and correo_send.validate(): # Post: envia el dato al servidor, los datos no son cacheados por el servidor
        print(correo_send.nombre.data)
        print(correo_send.email.data)
        print(correo_send.comment.data)
        
        #Mando una alerta al usuario "nombre" de que su mensaje fue enviado
        nombre= correo_send.nombre.data
        success_message = "Thanks {}, your message has been sended!".format(nombre)
        flash(success_message)
        
        return redirect(url_for("contact"))
    else:
        print("Error")

    titulo= "Marcial Barboza - Contact"
    return render_template("contact.html", tituloHTML= titulo, form= correo_send)

#PAGES PROJECTS
@app.route("/projects/theFrogsAdventure")
def p1frogs():
    titulo= "Marcial Barboza - The Frogs Adventure"
    return render_template ("/projects/p1frogs.html", tituloHTML= titulo)

@app.route("/projects/firstWebsite")
def p2website():
    titulo= "Marcial Barboza - My first website"
    return render_template ("/projects/p2website.html", tituloHTML= titulo)

if __name__ == "__main__":
    csrf.init_app(app)
    app.run