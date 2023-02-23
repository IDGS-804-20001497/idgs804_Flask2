from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField
from wtforms.fields import EmailField, TextAreaField, PasswordField, RadioField
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

class WordsForm(Form):
    spanish = StringField('Spanish')
    english = StringField('English')


class LoginForm(Form):
    username = StringField('usuario',
    [validators.DataRequired('El campo es requerido'),
    validators.length(min =5, max = 10, message = 'Ingresa min 5 max 10')])

    password = PasswordField('Contraseña',
    [validators.DataRequired('El campo es requerido'),
    validators.length(min =5, max = 10, message = 'Ingresa min 5 max 10')])


