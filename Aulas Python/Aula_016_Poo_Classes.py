class Evento:
    def altera_nome_evento(self, novo_nome):
        print("Altera nome do Evento")
        self.nome = novo_nome


ev = Evento()
ev.nome = "Aula de Python"
print(ev.nome)

ev.altera_nome_evento('Aula de JavaScript')
print(ev.nome)

