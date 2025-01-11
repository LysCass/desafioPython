def calcular_media():
    # Solicita o nome do aluno
    nome = input("Escreva seu nome: ")

    # Solicita as 4 notas
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    nota3 = int(input("Digite a terceira nota: "))
    nota4 = int(input("Digite a quarta nota: "))
    
    # Calcula a média aritmética
    media = (nota1 + nota2 + nota3 + nota4) / 4
    
    # Exibe o resultado 
    print(f"Aluno = {nome} // Media = {media:.1f}")

# Chama a função 
calcular_media()
