from jogador_base import Animal


# class Reptil(Animal):
#     def __init__(self, nome, idade, tipo_de_pele = "escamas"):
#         super().__init__(nome, idade)
#         self.tipo_de_pele = tipo_de_pele

#     def fazer_som(self):
#         return super().fazer_som()        

#     def movimentar(self):
#         return "O reptil está rastejando."


class Reptil(Animal):
    def __init__(self, nome, idade, tipo_de_pele = "escamas"):
        super().__init__(nome, idade)
        self.tipo_de_pele = tipo_de_pele

    def fazer_som(self):
        return super().fazer_som()        

    def movimentar(self):
        return "O reptil está rastejando."