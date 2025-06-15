from flask import Flask, jsonify,  render_template, request
from main import chamarChat
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/sendMessage', methods=['POST'])
def invokeChat():
     data = request.get_json()
     if not data:    
        return jsonify({"status": "alert", "msg": "Mensagem não encontrada"}), 400
    
     msg = chamarChat(data.get('msg'))
     response = {"status": "OK", "msg": msg}
     print('Chamou - <> ', data)
     return(response), 200


@app.route('/', methods=['GET'])
def inicio():
   return render_template('index.html')


if __name__ == "__main__":
    app.run(port=2020, debug=True)
