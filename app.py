from flask import Flask, render_template
from flask import request
from flask_wtf.csrf import CSRFProtect
import forms 
from collections import Counter


app = Flask(__name__)
app.config['SECRET_KEY'] = "ESTA ES UNA CLAVE ENCRIPTADA"
csrf = CSRFProtect()

@app.route("/formprueba")
def formprueba():

    return render_template("formprueba.html")

@app.route("/Alumnos", methods = ['GET', 'POST'])
def Alumnos():
    reg_alum = forms.UserForm(request.form)

    if request.method == 'POST':
        print(reg_alum.matricula.data)
        print(reg_alum.nombre.data)

    render_template('Alumnos.html', form = reg_alum)
    
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
    

if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True, port=3000) 