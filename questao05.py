def inverter_string(s):
    # Inicializa uma string vazia para armazenar a string invertida
    string_invertida = ""
    
    # Percorre a string original de trás para frente
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]  # Adiciona cada caractere à string invertida
    
    return string_invertida

# String de exemplo
string_original = input("Informe a string que deseja inverter: ")

# Inverter a string
resultado = inverter_string(string_original)

# Exibir o resultado
print(f"A string invertida é: {resultado}")
