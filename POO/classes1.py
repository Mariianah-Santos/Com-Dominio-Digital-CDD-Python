class Pessoa():
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade

    def falar(self, falar):
        print(f"{self.nome} esta falando {falar}")
    def pararFalar(self):
        print("Parou de falar")
    def comer(self, alimento, bebida):
        print(f"Estou comendo {alimento} e bebendo {bebida} e não posso falar")
    def pararComer(self):
        print("Parou de comer")
    def dormir(self):
        print("Não estou fazendo nada. Vou dormir")