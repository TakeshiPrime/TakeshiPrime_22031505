from flask import Flask, jsonify, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hola Bienvenido Profe Honorio, aquí su servidor Takeshi Prime a la orden"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
