from flask import Flask, render_template
from flask import request
from flask_wtf.csrf import CSRFProtect
from forms import * 
from collections import Counter
from flask import make_response
from flask import flash
import os

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
def traductor():
    
    words = form.WordsForm(request.forms)
    palabraEncontrada = ''
    if(request.method == 'POST' and words.validate()):
        btnGuardar = request.form.get('btnGuardar')
        btnTraducir = request.form.get('btnTraducir')
        if(btnGuardar == 'Guardar'):    
            file = open('palabras.txt', 'a')
            file.write('\n' + words.spanish.data.upper() + '\n' + words.english.data.upper())
            file.close()
        if(btnTraducir == 'Traducir'):
            opcion = request.form.get('translate')
            file = open('palabras.txt', 'r')
            palabras = [linea.rstrip('\n') for linea in file]
            if(opcion == 'spanish'):
                spanishWord = request.form.get('txtSpanish')
                for posicion in range(len(palabras)):
                    if(palabras[posicion] == spanishWord.upper()):
                        palabraEncontrada = palabras[posicion - 1]
            elif(opcion == 'english'):
                englishWord = request.form.get('txtEnglish')
                for posicion in range(len(palabras)):
                    if(palabras[posicion] == englishWord.upper()):
                        palabraEncontrada = palabras[posicion + 1]
                        print(palabraEncontrada)

    return render_template('traductor.html', form = words, palabraEncontrada = palabraEncontrada)

if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True, port=3000) 