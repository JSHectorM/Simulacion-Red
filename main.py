import time
import random
#import binascii


def agrRedundancia(listaPalabras, bitRed):
    listRedundante = []
    for i in range(len(listaPalabras)):
        palabra = listaPalabras[i]
        for j in range(bitRed):
            palabra.insert(2**j-1, "*")
        listRedundante.append(palabra)
    return listRedundante


def ruido(cadena):
    i = 7
    cadRuido = ""
    bloque = int((len(cadena))/8)
    for j in range(bloque):
        cadena2 = cadena[i-7:i]
        if(cadena[i] == "0"):
            cadena2 = cadena2 + "1"
            cadRuido = cadRuido + cadena2
        else:
            cadena2 = cadena2 + "0"
            cadRuido = cadRuido + cadena2
        i = i+8

    if ((len(cadena)) % 8 != 0):
        cadena2 = cadena[i-7:len(cadena)]
        cadRuido = cadRuido + cadena2
    return cadRuido


def dividirPalabras(tamaño, mensaje):
    palabras = []
    i = 0
    for j in range(int(len(mensaje)/tamaño)):
        palabra = mensaje[i:tamaño*(j+1)]
        palabra2 = list(palabra)
        palabras.append(palabra2)
        i = i+tamaño
    return palabras


def paridad(cadenaAuto):
    cadena = ''
    for j in range(len(cadenaAuto)):
        i = 0
        cadenaTemporal = cadenaAuto[j]
        while(i < len(cadenaTemporal)):
            if (i == 0):
                if(cadenaTemporal[2] != "*"):
                    cadena = cadena + str(cadenaTemporal[2])
                if(cadenaTemporal[4] != "*"):
                    cadena = cadena + str(cadenaTemporal[4])
                if(cadenaTemporal[6] != "*"):
                    cadena = cadena + str(cadenaTemporal[6])
                if(cadena.count("1") % 2 == 0):
                    cadenaTemporal[0] = "0"
                else:
                    cadenaTemporal[0] = "1"
            if (i == 1):
                if(cadenaTemporal[2] != "*"):
                    cadena = cadena + str(cadenaTemporal[2])
                if(cadenaTemporal[5] != "*"):
                    cadena = cadena + cadenaTemporal[5]
                if(cadenaTemporal[6] != "*"):
                    cadena = cadena + cadenaTemporal[6]
                if(cadena.count("1") % 2 == 0):
                    cadenaTemporal[1] = "0"
                else:
                    cadenaTemporal[1] = "1"
            if(i == 3):
                if(cadenaTemporal[4] != "*"):
                    cadena = cadena + cadenaTemporal[4]
                if(cadenaTemporal[5] != "*"):
                    cadena = cadena + cadenaTemporal[5]
                if(cadenaTemporal[6] != "*"):
                    cadena = cadena + cadenaTemporal[6]
                if(cadena.count("1") % 2 == 0):
                    cadenaTemporal[3] = "0"
                else:
                    cadenaTemporal[3] = "1"
            cadena = ''
            i = i+1
        j = j+1


def comproHamming(cadenaAuto):
    cadena = ''
    resultadosParidad = ''
    for j in range(len(cadenaAuto)):
        i = 0
        cadenaTemporal = cadenaAuto[j]
        while(i < len(cadenaTemporal)):
            if (i == 0):
                cadena = cadena + str(cadenaTemporal[0])
                cadena = cadena + str(cadenaTemporal[2])
                cadena = cadena + str(cadenaTemporal[4])
                cadena = cadena + str(cadenaTemporal[6])

                if(cadena.count("1") % 2 == 0):
                    resultadosParidad = resultadosParidad + str(0)
                else:
                    resultadosParidad = resultadosParidad + str(1)

            if (i == 1):
                cadena = ''
                cadena = cadena + str(cadenaTemporal[1])
                cadena = cadena + str(cadenaTemporal[2])
                cadena = cadena + str(cadenaTemporal[5])
                cadena = cadena + str(cadenaTemporal[6])

                if(cadena.count("1") % 2 == 0):
                    resultadosParidad = resultadosParidad + str(0)
                else:
                    resultadosParidad = resultadosParidad + str(1)
            if(i == 3):
                cadena = ''
                cadena = cadena + str(cadenaTemporal[3])
                cadena = cadena + str(cadenaTemporal[4])
                cadena = cadena + str(cadenaTemporal[5])
                cadena = cadena + str(cadenaTemporal[6])

                if(cadena.count("1") % 2 == 0):
                    resultadosParidad = resultadosParidad + str(0)
                else:
                    resultadosParidad = resultadosParidad + str(1)
            cadena = ''
            i = i+1
        j = j+1
        if(resultadosParidad.count(0) != 3):
            posicionError = convercionDecimal(resultadosParidad)
            if(cadenaTemporal[posicionError] == '0'):
                cadenaTemporal[posicionError] = '1'
            else:
                cadenaTemporal[posicionError] = '0'


def convercionDecimal(resultadosParidad):
    escritor = resultadosParidad
    cadenaInvertida = escritor[::-1]

    if(cadenaInvertida == '001'):
        return 0
    if(cadenaInvertida == '010'):
        return 1
    if(cadenaInvertida == '011'):
        return 2
    if(cadenaInvertida == '100'):
        return 3
    if(cadenaInvertida == '101'):
        return 4
    if(cadenaInvertida == '110'):
        return 5
    if(cadenaInvertida == '111'):
        return 6


# Codigo para  Codificar Manchester
def manchester(mensaje):

    array = []
    codificacion = []
    #codManch = [(len(mensaje)*2)]

    for j in range(int(len(mensaje))):

        array = mensaje[j]
        if(array == '0'):
            codificacion.append(1)
            codificacion.append(0)

        elif (array == '1'):
            codificacion.append(0)
            codificacion.append(1)

    codigo = ''.join(map(str, codificacion))

    return codigo

# Descodificacion
def desManchester(mensaje):

    array = []
    desCod = []
    i = 0

    for j in range(int(len(mensaje))):

        array.append(mensaje[j])

    while i < (len(mensaje)):
        if(array[i] == '1' and array[i+1] == '0'):

            desCod.append(0)

        elif(array[i] == '0' and array[i+1] == '1'):

            desCod.append(1)

        i += 2

    desCodigo = ''.join(map(str, desCod))

    return desCodigo


#MAIN

print("Simulador de un canal de comunicaciones \n")
time.sleep(1)
# Abrir archivo y mostrarlo
print("Abriendo documento txt...\n")
time.sleep(3)
f = open("prueba.txt", "r")
time.sleep(2)
print("Copiando contenido...\n")
time.sleep(2)
mensaje = f.read()
print("Imprimiendo texto...\n")
time.sleep(2)
print(mensaje)
time.sleep(2)
print("Cerrando documento\n")
f.close()
time.sleep(2)

# Convertir a Binario
print("Cambiando a binario...\n")
time.sleep(2)
mensaje = mensaje.encode()
binInt = int.from_bytes(mensaje, "big")
mensajeBin = bin(binInt)
print("Imprimir mennsaje en binario...\n")
time.sleep(2)
print(mensajeBin)
time.sleep(1)


#Codificacion Redundantes
#divide en 4 bits
listaPalabras = dividirPalabras(4,mensajeBin)
paridad(agrRedundancia(listaPalabras,3))
print("\n Gnerar bits redundantes... \n")
#print(listaPalabras)

#Generar strinng con cadena
#convertirString =''
#for j in range(len(listaPalabras)):
#    i=0
#    cadenaAux = listaPalabras[j]
#    while(i<len(cadenaAux)):
#        convertirString = convertirString + str(listaPalabras[i])
#       i+=1
#   j+=1

print(convertirString)

# Manchester

mensajeBin = manchester(mensajeBin)
f = open("manchester.txt", "w")
f.write(mensajeBin)
f.close()


# simular envio
print("Enviando documento\n")
time.sleep(2)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".\n")
time.sleep(1)
print("Mensaje enviado\n")
time.sleep(1)
print("Mensaje recibido\n")
time.sleep(1)


# Descodificar Manchester

mensajeBin = desManchester(mensajeBin)
f = open("desManchester.txt", "w")
f.write(mensajeBin)
f.close()


# convertir a texto
print("Convirtiendo binario a texto...\n")
time.sleep(2)
binInt = int(mensajeBin, 2)
byteNumero = binInt.bit_length() + 7 // 8
binArray = binInt.to_bytes(byteNumero, "big")
mensaje = binArray.decode()
print("Impriemndo mensaje original...\n")
time.sleep(2)
print(mensaje)
time.sleep(2)
# guardar documento recibido
print("Guardando documento recibido\n")
time.sleep(2)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".\n")

f = open("pruebaRec.txt", "w")
f.write(mensaje)
f.close()
time.sleep(2)
print("Documento guardado\n")
