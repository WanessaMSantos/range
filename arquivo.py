# Imprimir todos os números exceto o número 13 (laço 'for in ... range')

for i in range (1, 21):
    if (i == 13):
        continue
else:
    print (i)

#imprimir todos os números de 1 a 20 exceto o número 13 (laço 'while')

contador = 1
while (contador <= 20):
    if (i == 13):
        contador = contador + 1
    else:
        print(contador)
        contador = contador + 1

#imprimir todos os números em ordem descendente

for i in range (20, 0, -1):
    if(i == 13):
        continue
    else:
        print(i)



