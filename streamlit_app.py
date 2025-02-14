print("Calculador de vacaciones")

nombre = input("Ingrese su nombre: \n")
clave = int (input ("Ingrese su clave de empleado: \n"))


if clave == 1:
    
    antiguedad = float (input ("Ingrese su antiguedad laboral: \n"))

    if antiguedad >= 1 and antiguedad < 2:
        print("Le corresponden 6 días de vacaciones a", nombre)
    elif antiguedad >= 2 and antiguedad < 7:
        print("Le corresponden 14 días de vacaciones a", nombre)
    elif antiguedad >= 7:
        print("Le corresponden 20 días de vacaciones a", nombre)
    else:
        print("No le corresponden vacaciones a ", nombre)

elif clave == 2:
    
    antiguedad = float (input ("Ingrese su antiguedad laboral: \n"))
    
    if antiguedad >= 1 and antiguedad < 2:
        print("Le corresponden 7 días de vacaciones a", nombre)
    elif antiguedad >= 2 and antiguedad < 7:
        print("Le corresponden 15 días de vacaciones a", nombre)
    elif antiguedad >= 7:
        print("Le corresponden 22 días de vacaciones a", nombre)
    else:
        print("No le corresponden vacaciones")

elif clave == 3:

    antiguedad = float (input ("Ingrese su antiguedad laboral: \n"))
    
    if antiguedad >= 1 and antiguedad < 2:
        print("Le corresponden 10 días de vacaciones a", nombre)
    elif antiguedad >= 2 and antiguedad < 7:
        print("Le corresponden 20 días de vacaciones a", nombre)
    elif antiguedad >= 7:
        print("Le corresponden 30 días de vacaciones a", nombre)
    else:
        print("No le corresponden vacaciones a ", nombre)

else:
    print("La clave no existe")

