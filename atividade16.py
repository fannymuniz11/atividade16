# Crie um programa que receba o peso e a altura de uma pessoa e calcule o Índice de Massa Corporal (IMC). O programa deve classificar o IMC da pessoa de acordo com a tabela a seguir:
# Abaixo do peso: IMC < 18.5
# Peso normal: 18.5 ≤ IMC < 25
# Sobrepeso: 25 ≤ IMC < 30
# Obesidade: IMC ≥ 30

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura"))
imc = peso/(altura ** 2)

if imc < 18.5:
    classificação= "Abaixo do peso"

elif imc < 25:
    classificação = "peso normal"   
elif imc < 30:
    classificaçao= "sobre peso"

else:
    Classificação= "Obesidade"
    
    print("IMC:" , round( imc,2))
    print("classificação:") , classificação)
    




