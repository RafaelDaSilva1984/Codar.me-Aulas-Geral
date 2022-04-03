class Evento:
    def metodo_instancia(self):
        return ('método de instancia chamado', self)

    @classmethod
    def metodo_classe(cls):
        return('método de classe chamado', cls)

    @staticmethod
    def metodo_estatico():
        return ' Estático chamado'
    
ev = Evento()
a = ev.metodo_instancia()
print(a)

b = ev.metodo_classe()
print(b)

c = ev.metodo_estatico()
print(c)

