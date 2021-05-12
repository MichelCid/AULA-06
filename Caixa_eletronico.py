def area(larg=0, comp=0):
    area = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {area}m²')


L = float(input('Largura (m): '))
C = float(input('Comprimento (m): '))
area(L, C)