from flask import Flask, render_template, request

app = Flask(__name__)


@app.before_request
def before_request():
    print('Antes de la petición...')


@app.after_request
def after_request(response):
    print('Despues de la petición...')
    return response


# Metodo 1 de creacion de rutas de la aplicacion flask
"""@app.route('/')
def index():
    return 'Código Facilito'"""

# metodo 2 de creacion de rutasd de la aplicacion flask
def index():
    print('Estamos accediendo a la vista')
    # return render_template('/index.html', titulo='Index')
    data = {
        'titulo': 'Index',
        'encabezado': 'Bienvenido(a)'
    }
    return render_template('index.html', data=data)


@app.route('/contacto')
def contacto():
    data = {
        'titulo': 'Contacto',
        'encabezado': 'Bienvenido(a)'
    }
    return render_template('contacto.html', data=data)


@app.route('/saludo/<nombre>')
def saludo(nombre):
    # return 'Hola, codi!'
    return 'Hola, {0}!'.format(nombre)


@app.route('/suma/<int:valor1>/<int:valor2>')
def suma(valor1, valor2):
    return 'La suma es: {0}'.format((valor1+valor2))


@app.route('/perfil/<nombre>/<int:edad>')
def perfil(nombre, edad):
    return 'Tu nombre es: {0} y tu edad es: {1}'.format(nombre, edad)


@app.route('/lenguajes')
def lenguajes():
    data = {
        'hay_lenguajes': True,
        'lenguajes': ['PHP', 'Python', 'Kotlin', 'Java', 'C#', 'JavaScript']
    }
    return render_template('lenguajes.html', data=data)


@app.route('/datos')
def datos():
    # print(request.args)
    a = request.args.get('valor1')
    b = request.args.get('valor2')
    return 'estos son los datos: {0}, {1}'.format(a, b)


@app.route('/holamundo')
def hola_mundo():
    return 'hola mundo!'


if __name__ == '__main__':
    app.add_url_rule('/', view_func=index)
    app.run(debug=True)
