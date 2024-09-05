from jogador_base import Jogador

class Torneio(Jogador):
    def __init__(self, nickname1, nickname2):
        super().__init__(nickname)
        self.participante = nickname

    def fazer_som(self):
        return super().fazer_som()        

    def movimentar(self):
        if self.pode_voar == True:
            return "O passaro está voando."
        return "O pássaro está caminhando."