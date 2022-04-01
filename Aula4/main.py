#Aula 4
#Prof Erberto Sousa
#Conteúdo: Controle de Fluxo

#Exemplo: Cálcular a Média de um Aluno e exibir a situação: Aprovado ou Reprovado
#Para o Aluno ser aprovado a MEDIA precisa ser Maior ou Igual a 7,0
#Caso Contrário, Reprovado

nota1 = float(input("Digite a 1ªNota: "))
nota2 = float(input("Digite a 2ªNota: "))
nota3 = float(input("Digite a 3ªNota: "))

media = float((nota1+nota2+nota3)/3)

if media >= 7:
    print("Média:", media ,"\nAluno Aprovado")
elif media >=4 and media <7:
    print("Média:", media, "\nAluno em Recuperação")
else:
    print("Média:", media ,"\nAluno Reprovado")