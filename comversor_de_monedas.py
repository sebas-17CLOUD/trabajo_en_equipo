import os
os.system("cls")

print("este es un programa creado por Sebastián Naranjo, Raul, Johan Porras")
print("     comversor de monedas")
opcion = "si"
while opcion == "si":
    print("""cual moneda quieres comvertir?
    opciones

    USD a CRC <--> CRC a USD
    
    USD a LBS <--> LBS a USD
    
    USD a EUR <--> EUR a USD
          
    USD a YEN <--> YEN a USD
    
    USD a YUAN <--> YUAN a USD

    --------------------------------------------------------------

    CRC a USD <--> USD a CRC

    CRC a LBS <--> LBS a CRC
    
    CRC a EUR <--> EUR a CRC
    
    CRC a YEN <--> YEN a CRC
    
    CRC a YUAN <--> YUAN a CRC

    --------------------------------------------------------------

    LBS USD  <--> USD LBS

    LBS CRC <--> CRC LBS

    LBS a EUR <--> EUR a LBS

    LBS a YEN <--> YEN a LBS

    LBS a YUAN <--> YUAN a LBS

    -------------------------------------------------------------
 
    EUR a USD <--> USD a EUR

    EUR a CRC <--> CRC a EUR

    EUR a LBS <--> LBS a EUR

    EUR a YEN <--> YEN a EUR

    EUR a YUAN <--> YUAN a EUR
    
    --------------------------------------------------------------
    
    YEN a USD  USD a YEN

    YEN a CRC  CRC a YEN

    YEN a LBS  LBS a YEN

    YEN a EUR  EUR a YEN

    YEN a YUAN  YUAN a YEN

    ---------------------------------------------------------------

    YUAN a USD  USD a YUAN

    YUAN a CRC  CRC a YUAN

    YUAN a LBS  LBS a YUAN

    YUAN a EUR  EUR a YUAN

    YUAN a YEN  YEN a YUAN""")

    opcioncomversor=str(input())
    if opcioncomversor == "usd_a_crc" or opcioncomversor == "dolar_a_colon" or opcioncomversor == "dolares_a_colones":
       tener1=input("ingrese numero aqui para comvertir->")
       resultadocomversor1=tener1*642.08
       print(resultadocomversor1)
    elif opcioncomversor == "crc a usd" or opcioncomversor == "colon a dolar" or opcioncomversor == "dolares a colones:":
       tener2=input("ingrese numero aqui para comvertir->")
       resultadocomversor2=tener2*642.08
       print(resultadocomversor2)
    elif opcioncomversor == "usd a lbs" or opcioncomversor == "dolar a libra" or opcioncomversor == "dolares a libras":
       tener3=input("ingrese numero aqui para comvertir->")
       resultadocomversor3=tener3*0.76
       print(resultadocomversor3)
    elif opcioncomversor == "lbs a usd" or opcioncomversor == "libra a dolar" or opcioncomversor == "libras a dolares":
       tener4=input("ingrese numero aqui para comvertir->")
       resultadocomversor4=tener4*0.76
       print(resultadocomversor4)
    elif opcioncomversor == "usd a eur " or opcioncomversor == "dolar a euro" or opcioncomversor == "dolares a euros":
       tener5=input("ingrese numero aqui para comvertir->")
       resultadocomversor5=tener5*0.92
       print(resultadocomversor5)
    elif opcioncomversor == "eur a usd" or opcioncomversor == "euro a dolar" or opcioncomversor == "euros a dolares":
       tener6=input("ingrese numero aqui para comvertir->")
       resultadocomversor6=tener6*0.92
       print(resultadocomversor6)
    elif opcioncomversor == "usd a yen" or opcioncomversor == "dolar a yen" or opcioncomversor == "dolares a yenes":
       tener7=input("ingrese numero aqui para comvertir->")
       resultadocomversor7=tener7*114.91
       print(resultadocomversor7)
    elif opcioncomversor == "yen a usd" or opcioncomversor == "yen a dolar" or opcioncomversor == "yenes a dolares":
       tener8=input("ingrese numero aqui para comvertir->")
       resultadocomversor8=tener8*114.91
       print(resultadocomversor8)
    elif opcioncomversor == "usd a yuan" or opcioncomversor == "dolar a yuan" or opcioncomversor == "dolares a yuanes":
       tener9=input("ingrese numero aqui para comvertir->")
       resultadocomversor9=tener9*6.32
       print(resultadocomversor9)
    elif opcioncomversor == "yuan a usd" or opcioncomversor == "yuan a dolar" or opcioncomversor == "yuanes a dolares":
       tener10=input("ingrese numero aqui para comvertir->")
       resultadocomversor10=tener10*6.32
       print(resultadocomversor10)
       ##########################################################################
    elif opcioncomversor == "crc a lbs" or opcioncomversor == "colon a libra" or opcioncomversor == "colones a libras":
       tener11=input("ingrese numero aqui para comvertir->")
       resultadocomversor11=tener11*848.51
       print(resultadocomversor11)
    elif opcioncomversor == "lbs a crc" or opcioncomversor == "libra a colon" or opcioncomversor == "libras a colones":
       tener12=input("ingrese numero aqui para comvertir->")
       resultadocomversor12=tener12*848.51
       print(resultadocomversor12)
    elif opcioncomversor == "crc a eur" or opcioncomversor == "colon a euro" or opcioncomversor == "colones a euros":
       tener13=input("ingrese numero aqui para comvertir->")
       resultadocomversor13=tener13*0.0014
       print(resultadocomversor13)
    elif opcioncomversor == "eur a crc" or opcioncomversor == "euro a colon" or opcioncomversor == "euros a colones":
       tener14=input("ingrese numero aqui para comvertir->")
       resultadocomversor14=tener14*0.0014
       print(resultadocomversor14)
    elif opcioncomversor == "crc a yen" or opcioncomversor == "colon a yen" or opcioncomversor == "colones a yenes":
       tener15=input("ingrese numero aqui para comvertir->")
       resultadocomversor15=tener15*0.18
       print(resultadocomversor15)
    elif opcioncomversor == "yen a crc" or opcioncomversor == "yen a colon" or opcioncomversor == "yenes a colones":
       tener16=input("ingrese numero aqui para comvertir->")
       resultadocomversor16=tener16*0.18
       print(resultadocomversor16)
    elif opcioncomversor == "crc a yuan" or opcioncomversor == "colon a yuan" or opcioncomversor == "colones a yuanes":
       tener17=input("ingrese numero aqui para comvertir->")
       resultadocomversor17=tener17*504.94
       print(resultadocomversor17)
    elif opcioncomversor == "yuan a crc" or opcioncomversor == "yuan a colon" or opcioncomversor == "yuanes a colones":
       tener18=input("ingrese numero aqui para comvertir->")
       resultadocomversor18=tener18*504.94
       print(resultadocomversor18)
       ############################################################################
    elif opcioncomversor == "lbs a eur" or opcioncomversor == "libra a euro" or opcioncomversor == "libras a euros":
       tener19=input("ingrese numero aqui para comvertir->")
       resultadocomversor19=tener19*1.21
       print(resultadocomversor19)
    elif opcioncomversor == "eur a lbs" or opcioncomversor == "euro a libra" or opcioncomversor == "euros a libras":
       tener20=input("ingrese numero aqui para comvertir->")
       resultadocomversor20=tener20*1.21
       print(resultadocomversor20)
    elif opcioncomversor == "lbs a yen" or opcioncomversor == "libra a yen" or opcioncomversor == "libras a yenes":
       tener21=input("ingrese numero aqui para comvertir->")
       resultadocomversor21=tener21*151.77
       print(resultadocomversor21)
    elif opcioncomversor == "yen a lbs" or opcioncomversor == "yen a libra" or opcioncomversor == "yenes a libras":
       tener22=input("ingrese numero aqui para comvertir->")
       resultadocomversor22=tener22*151.77
       print(resultadocomversor22)
    elif opcioncomversor == "lbs a yuan" or opcioncomversor == "libra a yuan" or opcioncomversor == "libras a yuanes":
       tener23=input("ingrese numero aqui para comvertir->")
       resultadocomversor23=tener23*8.35
       print(resultadocomversor23)
    elif opcioncomversor == "yuan a lbs" or opcioncomversor == "yuan a libra" or opcioncomversor == "yuanes a libras":
       tener24=input("ingrese numero aqui para comvertir->")
       resultadocomversor24=tener24*8.35
       print(resultadocomversor24)
       #######################################################################################
    elif opcioncomversor == "eur a yen" or opcioncomversor == "euro a yen" or opcioncomversor == "euros a yenes":
       tener25=input("ingrese numero aqui para comvertir->")
       resultadocomversor25=tener25*124.95
       print(resultadocomversor25)
    elif opcioncomversor == "yen a eur" or opcioncomversor == "yen a euro" or opcioncomversor == "yenes a euros":
       tener26=input("ingrese numero aqui para comvertir->")
       resultadocomversor26=tener26*124.95
       print(resultadocomversor26)
    elif opcioncomversor == "eur a yuan" or opcioncomversor == "euro a yuan" or opcioncomversor == "euros a yuanes":
       tener27=input("ingrese numero aqui para comvertir->")
       resultadocomversor27=tener27*6.87
       print(resultadocomversor27)
    elif opcioncomversor == "yuan a eur" or opcioncomversor == "yuan a euro" or opcioncomversor == "yuanes a euros":
       tener28=input("ingrese numero aqui para comvertir->")
       resultadocomversor28=tener28*6.87
       print(resultadocomversor28)
       #######################################################################################
    elif opcioncomversor == "yen a yuan" or opcioncomversor == "yenes a yuanes":
       tener29=input("ingrese numero aqui para comvertir->")
       resultadocomversor29=tener29*0.055
       print(resultadocomversor29)
    elif opcioncomversor == "yuan a yen" or opcioncomversor == "yuanes a yenes":
       tener30=input("ingrese numero aqui para comvertir->")
       resultadocomversor30=tener30*0.055
       print(resultadocomversor30)
    else:
       print("alguna moneda que ingresastes no esta en este programa")
    opcion = input("deseas ir al inicio?")
print("programa finalizado")
print("te ha gustado nuestro programa?")
calificacion=str(input())
if calificacion == "si":
    print("enacantados que te haya gustado")
else:
    print("trataremos de mejorar y de crear mas programas que te puedan gusten")