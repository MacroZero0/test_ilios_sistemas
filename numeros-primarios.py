def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

contador = 0
soma_acumulada = 0
numeros_primos = []

print("Pressione Enter para adicionar 1 ao contador. Digite 'sair' para encerrar.")

while True:
    entrada = input()
    
    if entrada.lower() == 'sair':
        print(f"Contador final: {contador}")
        print(f"Soma acumulada final: {soma_acumulada}")
        print(f"Números primos acumulados: {numeros_primos}")
        break
    
    contador += 1

    if eh_primo(contador):
        numeros_primos.append(contador)

    if soma_acumulada < 21:
        soma_acumulada += contador
    else:
        # Quando a soma acumulada chegar a 21 ou mais, só adiciona 1
        soma_acumulada += 1
    
    print(f"Contador: {contador}, Soma acumulada: {soma_acumulada}")
    
    
        
