'''Faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que se encontram no intervalo de 1 a 500.'''

soma = 0 #função de acumulador
cont = 0
for num in range (1,501,2):
  if num%3==0:
    cont += 1 # cont recebe ele mesmo e soma um
    soma=soma+num
print (f'A soma dos {cont} valores solicitados é igual a {soma}.')