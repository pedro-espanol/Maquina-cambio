# Calculadora de cambio

ejecutar = True

while ejecutar == True:
    precio = float(input("Ingresa precio del producto: "))
    dinero = float(input("Ingresa dinero con el que se ha pagado: "))
    print()

    cambio = dinero - precio

    monedas_tipos = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]



    if precio > dinero:
        print(f"Falta dinero\nFaltan {cambio*-1} €")

    else:
        for moneda in monedas_tipos:
            if cambio == 0:
                break
            if cambio >= moneda:
                if moneda >= 5:
                    print(f"{int(cambio/moneda)} billetes de {moneda}€")

                else:
                    print(f"{int(cambio/moneda)} monedas de {moneda}€")


            cambio = round(cambio % moneda, 2)
    
    
    def seguir_pregunta():
        global ejecutar
        respuesta = input("\n¿Salir? (y/n): ")

        if respuesta == "y":
            ejecutar = False
        elif respuesta == "n":
            ejecutar = True
        else:
            seguir_pregunta()

    seguir_pregunta()