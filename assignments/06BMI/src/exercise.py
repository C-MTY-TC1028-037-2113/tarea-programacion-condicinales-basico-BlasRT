def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))
    if (altura<=0 or peso<=0):
        print("Revisa tus datos, alguno de ellos es erróneo.")
    else:
        indice=peso/(altura*altura)
        if (indice>=40):
            print("OBESIDAD MORBIDA")
        elif (30<=indice<40):
            print("OBESIDAD")
        elif (25<=indice<30):
            print("SOBREPESO")
        elif (20<=indice<25):
            print("NORMAL")
        else:
            print("PESO BAJO")
    

if __name__=='__main__':
    main()