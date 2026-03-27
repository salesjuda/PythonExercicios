#Escreva um programa para aprovar o emrpréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
valor_casa = float(input("Informe o valor da casa: "))
salario = float(input("Informe o valor do salário: "))
anos = int(input("Informe a quantidade de anos: "))
prestacao = valor_casa / (anos * 12)
if (prestacao > salario * 0.30):
    print("Emprestimo Negado!")
else:
    print("Emprestimo Aceito!")
print(f"o Valor da prestação é de: R${prestacao:.2f}")



