from tipo_mamifero import Mamifero
from torneio import Torneio
from tipo_reptil import Reptil

def main():
    jogadores = []
    
    while True:
        print("\nMenu:")
        print("1. Cadastrar Para Torneio")
        print("2. Consultar Animais")
        print("3. Remover Animal")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":

            tipo = input("Escolha o Tipo do Jogo (Luta, Corrida): ").strip().lower()
            
            jogador1 = input("Digite o nick do jogador 1: ")
            jogadores.append(jogador1)
            jogador2 = input("Digite o nick do jogador 2: ")
            jogadores.append(jogador2)
            print("Jogadores inscritos com sucesso no torneio!")

            if tipo == "luta":
                # pode_voar = input("O pássaro pode voar? Digite(sim/não): ").strip().lower() == "sim"
                vencedor_luta = Torneio(jogador1, jogador2, tipo)
                
            elif tipo == "corrida":
                tem_pelo = input("O mamífero tem pelo? (sim/não): ").strip().lower() == "sim"
                animal = Mamifero(nome, idade, tem_pelo)
            # elif tipo == "reptil":
            #     tipo_de_pele = input("Digite o tipo de pele do réptil (escamas, outro): ").strip()
            #     animal = Reptil(nome, idade, tipo_de_pele)
            else:
                print("Tipo de animal desconhecido.")
                continue
            
            # animais.append(animal)
            # print("Animal cadastrado com sucesso!")
        
        elif opcao == "2":
            if not jogadores:
                print("Nenhum animal cadastrado.")
            else:
                for i, animal in enumerate(jogadores):
                    print(f"{i + 1}. {animal} - Som: {animal.fazer_som()} - Movimento: {animal.movimentar()}")
        
        elif opcao == "3":
            if not jogadores:
                print("Nenhum animal cadastrado para remover.")
            else:
                for i, animal in enumerate(jogadores):
                    print(f"{i + 1}. {animal}")
                indice = int(input("Digite o número do animal para remover: ")) - 1
                if 0 <= indice < len(jogadores):
                    removido = jogadores.pop(indice)
                    print(f"Animal removido: {removido}")
                else:
                    print("Número inválido.")
        
        elif opcao == "4":
            print("Encerrado...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()