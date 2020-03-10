import time
#import binascii

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
