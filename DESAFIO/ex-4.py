class Carro():
    def __init__(self, modelo, marca, ano, cor, valor, qtd_portas):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.valor = valor
        self.qtd_portas = qtd_portas
    def acelerar(self):
        print("Aelerando...")
    def frear(self):
        print("Freiando...")
    def buzinar(self):
        print("Buzinando...")

carro_celta = Carro("HB20K", "Celta", 2021, "Preto", 34.999, 4)
print(f"MODELO: {carro_celta.modelo} \nMARCA: {carro_celta.marca} \nANO: {carro_celta.ano}", end=" ")
print(f"VALOR R${carro_celta.valor} \nCOR: {carro_celta.cor} \nPORTAS: {carro_celta.qtd_portas}")
carro_celta.acelerar()
carro_celta.frear()
carro_celta.buzinar()