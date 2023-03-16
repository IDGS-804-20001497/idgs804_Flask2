from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField,EmailField,PasswordField
from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms.fields import FieldList
from wtforms import validators
from wtforms.validators import DataRequired


def mi_validacion(form, field):
    if len(field.data) == 0:
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):
    matricula = StringField('Matricula',
    [validators.DataRequired('El campo es requerido'),
    validators.length(min =5, max = 10, message = 'Ingresa min 5 max 10')])

    nombre = StringField('Nombre',
    [validators.DataRequired(message = 'El campo matricula es requerido ')])

    apaterno = StringField('Apaterno', [
        mi_validacion
    ])
    amaterno = StringField('Amaterno')
    email = EmailField('Correo')
    numero = StringField('Numero')

class WordForm(FlaskForm):
    spanish_word = StringField('Palabra en español', validators=[DataRequired()])
    english_word = StringField('Palabra en inglés', validators=[DataRequired()])
    submit = SubmitField('Guardar')

class TranslateForm(FlaskForm):
    word = StringField('Palabra a traducir', validators=[DataRequired()])
    language = RadioField('Idioma', choices=[('english', 'Inglés'), ('spanish', 'Español')], default='english')
    submit = SubmitField('Traducir')

class ResistenciaForm(FlaskForm):
    opciones_banda = [("negro", "Negro"), ("marron", "Marrón"), ("rojo", "Rojo"), ("naranja", "Naranja"),
                      ("amarillo", "Amarillo"), ("verde", "Verde"), ("azul", "Azul"), ("violeta", "Violeta"),
                      ("gris", "Gris"), ("blanco", "Blanco")]

    opciones_tolerancia = [("oro", "Oro"), ("plata", "Plata")]

    banda1 = SelectField("Banda 1", choices=opciones_banda, validators=[DataRequired()])
    banda2 = SelectField("Banda 2", choices=opciones_banda, validators=[DataRequired()])
    banda3 = SelectField("Banda 3", choices=opciones_banda, validators=[DataRequired()])
    tolerancia = RadioField("Tolerancia", choices=opciones_tolerancia, validators=[DataRequired()])
    calcular = SubmitField("Calcular")

class LoginForm(Form):
    username = StringField('usuario',
    [validators.DataRequired('El campo es requerido'),
    validators.length(min =5, max = 10, message = 'Ingresa min 5 max 10')])

    password = PasswordField('Contraseña',
    [validators.DataRequired('El campo es requerido'),
    validators.length(min =5, max = 10, message = 'Ingresa min 5 max 10')])
