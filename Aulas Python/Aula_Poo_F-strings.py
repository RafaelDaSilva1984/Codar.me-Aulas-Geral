class Evento:
    id = 1 # atributo de classe q compartilhado entre as instancias das classes

    def __init__(self, nome, local=''):
        self.nome = nome
        self.local = local
        self.id = Evento.id
        Evento.id += 1

    def impreme_informações(self):
        print(f'Id do evento:{self.id}')
        print(f'Nome do evento:{self.nome}')
        print(f'Local do evento:{self.local}')
        print('----------------------------')

    @classmethod
    def cria_evento_online(cls, nome):
        evento = cls(nome, local=f'https://tamarcado.com/eventos?id={cls.id}')
        return evento

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

ev_online = Evento.cria_evento_online('Live de Python')
ev2_online = Evento.cria_evento_online('Live de JavaScript')
ev_online.impreme_informações()
ev2_online.impreme_informações()





