from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quienes')
def quienes():
    return render_template('quienes.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        print("Formulario enviado:", request.form)
    return render_template('contacto.html')

@app.route('/servicio1')
def servicio1():
    return render_template('servicio1.html')

@app.route('/servicio2')
def servicio2():
    return render_template('servicio2.html')

@app.route('/servicio3')
def servicio3():
    return render_template('servicio3.html')

if __name__ == '__main__':
    app.run(debug=True)