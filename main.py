string1=input()
string2=input()

vetor1 = string1.split(' ')
vetor2 = string2.split(' ')

codigo1 = int(vetor1[0])
numero1 = int(vetor1[1])
valor1 = float(vetor1[2])

codigo2 = int(vetor2[0])
numero2 = int(vetor2[1])
valor2 = float(vetor2[2])

valortotal = (valor1*numero1)+(valor2*numero2)

print("VALOR A PAGAR: R$ %0.2f"%valortotal)
