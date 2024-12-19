seg1 = float(input('Informe o 1° segmento: '))
seg2 = float(input('Informe o 2º segmento: '))
seg3 = float(input('Informe o 3° segmento: '))
if seg1 < seg2 + seg3 and seg2 < seg3 + seg1 and seg3 < seg1 + seg2:
    print("Os segmentos acima podem formam um Triangulo !")
    if seg1 == seg2 == seg3:
        print('Triangulo EQUILATERO !!')
    elif seg1 != seg2 and seg2 != seg3 and seg3 != seg1:
        print('Triangulo ESCALENO !!')
    else:
        print('Triangulo ISOCELES !!')
else:
    print('Os segmento NAO formam um triangulo !!')
