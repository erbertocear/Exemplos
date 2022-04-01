contador = 0
soma = 0

while contador <3:
    #Contando o numero de vezes que entrou no laço
    contador+=1
    #Aqui estamos pedindo para o usuário digital um numero
    num = int(input("Digite um numero: "))
    #Estamos realizando a soma
    soma = soma + num

print("O resultado final da soma: ", soma)