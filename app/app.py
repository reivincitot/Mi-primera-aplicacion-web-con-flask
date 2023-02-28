from flask import Flask, render_template

app = Flask(__name__)

# Metodo 1 de creacion de rutas de la aplicacion flask

"""@app.route('/')
def index():
    return 'Código Facilito'"""

# metodo 2 de creacion de rutasd de la aplicacion flask


def index():
    #return render_template('/index.html', titulo='Index') 
    data = {
        'titulo' : 'Index',
        'encabezado':'Bienvenido'
    }

def hola_mundo():
    return 'hola mundo!'


if __name__ == '__main__':
    app.add_url_rule('/hola_mundo', view_func=hola_mundo)
    app.add_url_rule('/', view_func=index)
    app.run(debug=True)
