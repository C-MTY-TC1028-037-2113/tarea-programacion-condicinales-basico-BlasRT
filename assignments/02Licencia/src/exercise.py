def main():
    edad = int(input("Ingresa tu edad: "))
    if (edad<=0):
        print("Respuesta incorrecta")
    elif (0<edad<18):
        print("No cumples requisitos")
    else:
        id = str(input("¿Tienes identificación oficial? (s/n): "))
        if (edad>=18 and id=="s"):
            print("Trámite de licencia concedido")
        elif (edad>=18 and id=="S"):
            print("Trámite de licencia concedido")
        elif (0<=edad<18 or id=="n" or id=="N"):
            print("No cumples requisitos")
        else:
            print("Respuesta incorrecta")    
    #Aquí empieza tu programa...


if __name__ == '__main__':
    main()
