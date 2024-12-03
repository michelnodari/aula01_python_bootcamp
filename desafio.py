#Questão: Cálculo de Bônus com Entrada do Usuário
#Escreva um programa em Python que solicita ao usuário para digitar seu nome, 
# o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, 
# imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação
#  com o bônus recebido.

CONSTANTE_BONUS = 1000
#Instruções:
# 1) O programa deve começar solicitando ao usuário que insira seu nome.
nome_usuario = input("Digite o Seu Nome: ")

# 2) Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.

val_salario = float(input("Informe o valor do seu salário: "))

# 3) Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.

percent_bonus = float(input("Informe a porcentagem do bônus recebido: ") )

# 4) O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus

valor_do_bonus = CONSTANTE_BONUS + (val_salario * percent_bonus)

# 5) Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
print(f"Olá {nome_usuario}, o seu valor bônus foi de {valor_do_bonus}.")

