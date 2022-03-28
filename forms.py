from wtforms import Form, validators
from wtforms import StringField, TextAreaField,EmailField
from wtforms.validators import InputRequired,Email,Length

#Formularios
class correo(Form):
    nombre = StringField("Name", validators=[InputRequired(),Length(min=4,max=25,message="Ingrese nombre correcto"),],render_kw={"placeholder": "Alex"})

    email = EmailField("Email", validators=[InputRequired(),Email(message="Ingrese un email válido")],render_kw={"placeholder": "example@email.com"})
       
    comment = TextAreaField("Comentario", validators=[InputRequired(),Length(min=10,max=200,message="Ingrese un comentario válido")],render_kw={"placeholder":"Hey, i want to talk with you!"})

#Validador del honeypot (antibots)
def length_honeypot(form, field):
    if len(field.data)>0:
        raise validators.ValidationError("El campo debe estar vacío")

# ANTI BOTS
honeypot = TextAreaField("", [length_honeypot])