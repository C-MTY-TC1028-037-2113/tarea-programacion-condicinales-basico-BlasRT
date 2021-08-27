def main():
    X = int(input("Ingresa la medida del lado 1: "))
    Y = int(input("Ingresa la medida del lado 2: "))
    Z = int(input("Ingresa la medida del lado 3: "))
    #Escribe aquí tu código...
    if (X<=0 or Y<=0 or Z<=0):
        print("NO ES TRIANGULO")
    elif (X+Y<Z or X+Z<Y or Y+Z<X):
        print("NO ES TRIANGULO")
    elif (X==Y and Y==Z):
        print("ES UN TRIANGULO EQUILATERO")
    else:
        if (X==Y or X==Z or Y==Z):
            print("ES UN TRIANGULO ISOSCELES")
        else:
            print("ES UN TRIANGULO ESCALENO")
            
if __name__=='__main__':
    main()
