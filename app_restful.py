from flask import Flask
from flask_restful import Resource, Api, request
import json
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {"Nome": "Ully",
     "Habilidades": ["React, Angular, Javascript"]},

    {"Nome": "Camila",
     "Habilidades": ["Javascript, Nodejs"]},
    {"Nome": "Douglas",
     "Habilidades": ["Python, Flask, javascript"]}

]


class desenvolvedor(Resource):

    def get (self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            message = 'Desenvolvedor {} não localizado'.format(id)
            response = {"status": 400, "message": message}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {"status": "200", "messege": "item removed successful"}


class lista_desenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(desenvolvedor, '/dev/<int:id>')
api.add_resource(lista_desenvolvedores, '/dev')
api.add_resource(Habilidades, '/habilidades')

if __name__ == '__main__':
    app.run(debug=True)