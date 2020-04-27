from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {"Nome": "Ully",
     "Habilidades": ["React, Angular, Javascript"]},

    {"Nome": "Camila",
     "Habilidades": ["Javascript, Nodejs"]},
    {"Nome": "Douglas",
     "Habilidades": ["Python, Flask, javascript"]}

]


# Remove, atualiza, e busca o dado atraves do id
@app.route("/dev/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            message = 'Desenvolvedor {} não localizado'.format(id)
            response = {"status": 400, "message": message}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({"status": "200", "messege": "item removed successful"})


# Lista todos os desenvolvedores e registrar novos devs
@app.route("/dev", methods=['POST', 'GET'])
def lista_desenvolvedor():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({"status": 200, "mensagem": "Desenvolvedor cadastrado"})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)
