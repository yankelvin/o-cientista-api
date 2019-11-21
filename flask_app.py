from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
import json
from cykParser import CykParser

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def hello():
    return "App rodando!"


@app.route('/api/cykParser', methods=['POST'])
@cross_origin()
def question():
    if request.method == 'POST':
        data = request.json
        word = data['word']
        grammar = data['grammar']

        parser = CykParser(word, grammar)

        result = parser.filling_matrix()
        return json.dumps(result)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
