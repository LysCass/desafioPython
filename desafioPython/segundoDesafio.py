import re

def maior_letra(string):
    # Remover caracteres não alfanuméricos e converter para minúsculas
    string = re.sub(r'[^a-zA-Z]', '', string).lower()
    
    # Encontrar a maior letra
    maior = max(string)
    
    # Exibir a maior letra
    print(f"Maior letra = '{maior}'")

# Testes com as entradas
entrada1 = 'gosto de cafe sem acucar'
entrada2 = 'vamos ver um filme semana que vem'
entrada3 = 'coma mais verduras'

maior_letra(entrada1)
maior_letra(entrada2)
maior_letra(entrada3)
