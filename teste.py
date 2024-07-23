from classe import Carro

def teste_veiculos():
    carro = Carro("Toyota", "Gasolina")
    carro.dirigir(150)
    print(f"Marca: {carro.marca}, Tipo: {carro.tipo_combustivel}")
    print(f"Quilometragem: {carro.get_quilometragem()} km")
    print(f"Ano do veículo: {carro.get_ano()}")
    carro.abastecer()
    

teste_veiculos()