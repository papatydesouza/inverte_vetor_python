print("******* Olá! Bem vindo ao Jogo Inverte Vetor ********")

listaNumerosReais = []
print ('Informe os 10 números e pressione enter entre eles: ')
for i in range(10):
    listaNumerosReais.append(float(input('Numero '+ str(i+1) + ':\n')))
print (listaNumerosReais)
listaNumerosReais.reverse()
print (listaNumerosReais)