from evento import Evento

class EventoOnline(Evento):
    def __init__(self, nome, local_=''):
        local = f'https://tamarcado.com/eventos?id={EventoOnline.id}'
        super().__init__(nome, local)

    def imprime_informações(self):
        print(f'Id do evento:{self.id}')
        print(f'Nome do evento:{self.nome}')
        print(f'Link para acessar o Evento:{self.local}')
        print('----------------------------')    
  