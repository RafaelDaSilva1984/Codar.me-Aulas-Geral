
import json

class Evento:
    id = 1 # atributo de classe q compartilhado entre as instancias das classes

    def __init__(self, nome, local=''):
        self.nome = nome
        self.local = local
        self.id = Evento.id
        Evento.id += 1

    def imprime_informações(self):
        print(f'Id do evento: {self.id}')
        print(f'Nome do evento: {self.nome}')
        print(f'Local do evento: {self.local}')
        print('----------------------------')

    def to_json(self):
        return json.dumps({

            "id": self.id,
            "local": self.local,
            "nome": self.nome
        })
  
    @staticmethod
    def calcula_limite_pessoas_area(area):
        if 5 <= area < 10:
            return 5
        elif 10 <= area < 20:
            return 10
        elif 20 <= area < 30:
            15
        else:
            return 0




