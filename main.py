import time
#import binascii

#Codigo para  Codificar Manchester
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




print ("Simulador de un canal de comunicaciones \n")
time.sleep(1)
#Abrir archivo y mostrarlo
print("Abriendo documento txt...\n")
time.sleep(3)
f = open ("prueba.txt", "r")
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

#Convertir a Binario
print("Cambiando a binario...\n")
time.sleep(2)
mensaje = mensaje.encode()
binInt = int.from_bytes(mensaje, "big")
mensajeBin = bin(binInt)
print("Imprimir mennsaje en binario...\n")
time.sleep(2)
print (mensajeBin)
time.sleep(1)



#Codificacion manchester

mensajeBin = manchester(mensajeBin)
f = open ("manchester.txt", "w")
f.write (mensajeBin)
f.close()


#simular envio
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


#Descodificar Manchester

mensajeBin = desManchester(mensajeBin)
f = open ("desManchester.txt", "w")
f.write (mensajeBin)
f.close()



#convertir a texto
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
#guardar documento recibido
print("Guardando documento recibido\n")
time.sleep(2)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".\n")

f = open ("pruebaRec.txt", "w")
f.write (mensaje)
f.close()
time.sleep(2)
print("Documento guardado\n")
