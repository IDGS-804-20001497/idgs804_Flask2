from flask import Flask, render_template
from flask import request
from flask_wtf.csrf import CSRFProtect
import forms
from collections import Counter
from flask import make_response
from flask import flash
import os
from flask import Flask, render_template, request
from forms import WordForm, TranslateForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "ESTA ES UNA CLAVE ENCRIPTADA"
csrf = CSRFProtect()

@app.route("/cookie", methods = ['GET', 'POST'])
def cookie():
    reg_user = forms.LoginForm(request.form)
    response = make_response(render_template('cookie.html', form = reg_user,))

    if request.method == 'POST' and reg_user.validate():
        user = reg_user.username.data
        password = reg_user.password.data
        datos = user + '@' + password
        success_message = 'Bienvenido {}'.format(user)
        response.set_cookie('datos_usuario', datos)
        flash(success_message)
    return response

@app.route("/formprueba")
def formprueba():

    return render_template("formprueba.html")

@app.route("/Alumnos", methods=['GET','POST'])
def Alumnos():
    reg_alum=forms.UserForm(request.form)
    datos=list()
    if request.method == 'POST' and reg_alum.validate():
        datos.append(reg_alum.matricula.data)
        datos.append(reg_alum.nombre.data)
        print(reg_alum.matricula.data)
        print(reg_alum.nombre.data)

    return render_template("Alumnos.html",form=reg_alum, datos=datos)
    
@app.route("/", methods=['GET','POST'])
def cajasDinamicas():
    reg_alum=forms.UserForm(request.form)

    if request.method == 'POST':
        numero = int(reg_alum.numero.data)
        return render_template("CajasDinamicas.html", numero = numero, form = reg_alum)
    else:
        return render_template("CajasDinamicas.html", form = reg_alum)

@app.route("/Calculos", methods=['GET','POST'])
def Calculos():
    reg_alum = forms.UserForm(request.form)
    lista = request.form.getlist("txtNum")
    maxim = int(lista[0])

    for x in lista:
        if int(maxim) > int(x):
            maxim = maxim
        else:
            maxim = x
   
    minimo = int(lista[0])

    for m in lista:
        if int(minimo) < int(m):
            minimo = minimo
        else:
            minimo = m
    suma=0
    for valor in lista:
        suma = suma + int(valor)
    cant = len(lista)
    promedio = suma / cant

    conteo = Counter(lista)
    resultado = {}
    for n in conteo:  
        val = conteo[n]
        resultado[n] = val
    
    return render_template("Calculos.html", lista = lista, maxim = maxim, minimo = minimo, promedio = promedio, resultado = resultado)
    
@app.route('/traductor', methods=['GET', 'POST'])
def index():
    word_form = WordForm()
    translate_form = TranslateForm()

    if word_form.validate_on_submit():
        with open('palabras.txt', 'a') as f:
            f.write(f'{word_form.spanish_word.data.lower()}={word_form.english_word.data.lower()}\n')
        return render_template('traductor.html', word_form=word_form, translate_form=translate_form, message='Guardado con éxito')

    if translate_form.validate_on_submit():
        language = translate_form.language.data
        with open('palabras.txt') as f:
            words = dict(line.strip().lower().split('=') for line in f)
            try:
                if language == 'english':
                    translation = words[translate_form.word.data.lower()]
                else:
                    translation = [key for key, value in words.items() if value == translate_form.word.data.lower()][0]
                message = f'Traducción: {translation}'
            except (KeyError, IndexError):
                message = 'No se encuentra la traducción'
        return render_template('traductor.html', word_form=word_form, translate_form=translate_form, message=message)

    return render_template('traductor.html', word_form=word_form, translate_form=translate_form)


if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True, port=3000) 