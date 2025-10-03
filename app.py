from flask import Flask, jsonify, request, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

# Página principal con parámetro opcional (?nombre=)
@app.route('/', methods=['GET'])
def index():
    nombre = request.args.get('nombre', None)
    return render_template('index.html', nombre=nombre)

# Endpoint JSON que usa parámetro (?nombre=)
@app.route('/api/hello', methods=['GET'])
def hello():
    nombre = request.args.get('nombre', 'Invitado')
    return jsonify({
        "saludo": f"Hola {nombre}, aquí su servidor Takeshi Prime a la orden",
        "autor": "Takeshi Prime (Ramón Alejandro Castro Noriega)"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
