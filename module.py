def feladat01():
    szam:int = int(input(f'Kérek egy számot: '))
    betu:str = input(f'Kérek egy szöveget: ')

    szam ** 2
    betu.lower
    print(betu, " " * szam)


def feladat02():
    a:float = float(input('\tAz első szám: '))
    b:float = float(input('\tA második szám: '))
    c:float = float(input('\tA harmadik szám: '))

    if a + b > c or a + c > b or b + c > a:
        print('A háromszög szerkeszthető')
    
        if a == b or b == c or c == a :
            print('Ez a háromszög egyenlő szárú')

        else: print('Ez a háromszög nem egyenlő szárú')

        kerulet = a + b + c
        terulet = a * b / 2

        if (a * a + b * b) == c * c or (a * a + c * c) == b * b or (b * b + c * c) == a * a:
            print('Ez a háromszög derékszögű')

            print(f'A szerkeszthető háromszög kerülete: {kerulet}')
            print(f'A háromszög területe: {terulet}')

    else: print('A háromszög nem szerkeszthető')


#class bolygo:
#def feladat03():
