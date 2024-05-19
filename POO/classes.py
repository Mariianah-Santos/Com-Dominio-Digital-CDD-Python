class Pessoa():
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade

        self.falando = False
        self.comendo = False
        self.dormindo = False

    def falar(self):
        if self.falando:
            print("Não estou falando")
        else:
            print("Estou conversando")
            self.falando = True
            self.dormindo = True
            self.comendo = True

    def comer(self):
        if self.comendo:
            print("Não posso comer")
        else:
            print("Estou comendo")
            self.comendo = True
            self.falando = True
            self.dormindo = True

    def dormir(self):
        if self.dormindo:
            print("Não estou dormindo")
        else:
            print("Estou dormindo")
            self.dormindo = True
            self.comendo = True
            self.falando = True
