equipamentos = []
valores = []
seriais = []
departamento = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamentos: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número serial: ")))
    departamento.append(input("digite o departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

busca=input("\nDigite o nome do equipamento que deseja buscar: ")
for indice in range(0,len(equipamentos)):
    if busca==equipamentos[indice]:
        print("Valor..: ", valores[indice])
        print("Serial.: ", seriais[indice])
