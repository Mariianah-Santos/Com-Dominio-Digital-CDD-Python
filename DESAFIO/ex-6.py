class Computador():
    def __init__(self, marca, cor, memoria, armazenamento):
        self.marca = marca
        self.cor = cor
        self.memoria = memoria
        self.armazenamento = armazenamento
    
    def ligar(self):
        print("PC esta Ligado")

    def desliga(self):
        print("Desligado")
        
    def reiniciar(self):
        print("Reiniciando...")

pc_hp = Computador("HP", "Prata", 4, 256)
pc_hp.ligar()
pc_hp.desliga()
pc_hp.desliga()
