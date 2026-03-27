#Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00 calcule um aumento de 10%.
#Para os inferiores ou iguai, o aumento é de 15%.
salario = float(input("Digite o valor do seu salário: "))
if(salario >= 1250):
    aumento = salario * 0.10
    novo_salario = aumento + salario
else:
    aumento = salario * 0.15
    novo_salario = aumento + salario
print(f"O seu Salário é: {salario:.2f}")
print(f"O seu aumento é de: {aumento:.2f}")
print(f"O seu novo salário é de: {novo_salario:.2f}")
