class Veiculo:
    def __init__(self, marca):
        self.marca = marca             
        self._ano = 2020               
        self.__quilometragem = 0       

    def dirigir(self, distancia):
        self.__quilometragem += distancia

    def get_quilometragem(self):
        return self.__quilometragem


class Carro(Veiculo):
    def __init__(self, marca, tipo_combustivel):
        super().__init__(marca)
        self.tipo_combustivel = tipo_combustivel  

    def abastecer(self):
        print(f"Abastecendo o carro {self.marca} .")

    def get_ano(self):
        return self._ano  
