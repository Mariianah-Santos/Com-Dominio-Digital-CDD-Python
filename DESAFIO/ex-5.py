class Carro():
    def __init__(self, marca, cor, ano):
        self.marca = marca
        self.cor = cor
        self.ano = ano

        self.ligado = False
        self.velociadade = 0
    def ligar(self):
        if self.ligado:
            print("carro esta ligado")
        else:
            print("Ligando o carro...")
            self.ligado = True

    def desligar(self):
        if self.ligado:
            print("carro esta desligado")
            self.ligado = False
        else:
            print("Desligando Carro...")
    def movimentar(self):
        if self.ligado:
            self.velociadade += 1
            print(f"Velocidade: {self.velociadade} km")
        else:
            print("Não pode movimentar o carro. Carro desligado")

carro_celta = Carro("Celta", "Branco", 2021)
print(f"MARCA: {carro_celta.marca} \nCOR: {carro_celta.cor} \nANO: {carro_celta.ano}")
carro_celta.ligar()
carro_celta.ligar()
