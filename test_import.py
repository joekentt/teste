# test_import.py
try:
    from jogador_base import Animal
    from torneio import Ave
    from tipo_mamifero import Mamifero
    from tipo_reptil import Reptil
    print("Importações bem-sucedidas!")
except ImportError as e:
    print(f"Erro de importação: {e}")