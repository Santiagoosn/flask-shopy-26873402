from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
#Formulario de registro 
#de nuevo producto 
class NewProductForm(FlaskForm): 
    nombre = StringField("ingrese nombre: ")
    precio = StringField("ingrese precio: ")
    submit = SubmitField("Registro")