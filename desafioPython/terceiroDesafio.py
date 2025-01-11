def formatar_nome(nome_completo):
    # Divide o nome completo em partes
    partes = nome_completo.split()
    
    # O último sobrenome no final
    sobrenome = partes[-1].upper()
    
    # As primeiras letras dos outros nomes em maiúsculo
    iniciais = [p[0].upper() + '.' for p in partes[:-1]]
    
    # Junta o sobrenome e as iniciais 
    resultado = f"{sobrenome}, {' '.join(iniciais)}"
    
    return resultado

# Testes 
entrada1 = 'Fernanda Torres'
entrada2 = 'Lorrayne Bento'
entrada3 = 'Edgar Allan Poe'

print(formatar_nome(entrada1))  
print(formatar_nome(entrada2))  
print(formatar_nome(entrada3))  
