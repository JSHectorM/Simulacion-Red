import random
#from matplotlib import *
import time

def lee(nombre):
	archivo = open(nombre,"r")
	mensaje = archivo.read()
	archivo.close()
	return mensaje

def escribe(nombre,mensaje,escritura):
	archivo = open (nombre,escritura)
	archivo.write(mensaje)
	archivo.close()		

def cadenaBits(tamaño):
	i=1;
	cadena = ""	
	while (i<=tamaño):
		cadena = cadena + str(random.randrange(2))
		#if i%8 == 0:
			#cadena = cadena + " "
		i=i+1
	return cadena

def codmanchester():
	#0 = nivel bajo 1= nivel alto
	escribe("bits.txt",cadenaBits(32),"w")
	cadena = lee("bits.txt")
	i=0;
	indice = ""
	codificado = ""
	for bit in cadena:
		i=i+1
		indice = str(i)
		if(bit == "0"):
			codificado = codificado + "-1"
		else:
			codificado = codificado + "0"	
	return codificado

def ruido(cadena):
	i=7;
	cadRuido= ""
	bloque = int((len(cadena))/8)
	for j in range(bloque):
		cadena2=cadena[i-7:i]
		if(cadena [i] == "0"):
			cadena2 = cadena2 + "1"
			cadRuido = cadRuido + cadena2
		else:	
			cadena2 = cadena2 + "0"		
			cadRuido = cadRuido + cadena2		
		i=i+8

	if ((len(cadena)) % 8 != 0):
		cadena2 = cadena[i-7:len(cadena)]
		cadRuido = cadRuido + cadena2		
	return cadRuido

def convBinario(mensaje):
	mensaje = mensaje.encode()
	binInt = int.from_bytes(mensaje,"big")
	mensajeBin = bin(binInt)
	return mensajeBin

def convTexto(mensaje):
	binInt = int(mensaje,2)
	byteNumero = binInt.bit_length() + 7 // 8
	binArray = binInt.to_bytes(byteNumero,"big")
	mensaje = binArray.decode()
	print (mensaje)
	return mensaje

def palabras(tamaño,mensaje):
	palabras=[];
	i= 0;
	for j in range(int(len(mensaje)/tamaño)):
		palabra =mensaje[i:tamaño*(j+1)]
		palabra2 = list(palabra)
		palabras.append(palabra2)
		i=i+tamaño
	return palabras

def agrRedundancia(listaPalabras,bitRed):
	listRedundante= [];
	for i in range(len(listaPalabras)):
		palabra = listaPalabras[i]
		for j in range(bitRed):
			palabra.insert(2**j-1,"*")
		listRedundante.append(palabra)
	return listRedundante		



def paridad (cadenaAuto):
	cadena = ''
	for j in range(len(cadenaAuto)):
		i=0
		cadenaTemporal = cadenaAuto[j]
		while(i<len(cadenaTemporal)):
			if (i==0):
				if(cadenaTemporal[2]!="*" ):
					cadena = cadena + str(cadenaTemporal[2])
				if(cadenaTemporal[4]!="*" ):
					cadena = cadena + str(cadenaTemporal[4])
				if(cadenaTemporal[6]!="*" ):
					cadena = cadena + str(cadenaTemporal[6])
				if(cadena.count("1")%2==0):
					cadenaTemporal[0]= "0"
				else:
					cadenaTemporal[0]= "1"	
			if (i==1):
				if(cadenaTemporal[2]!="*" ):
					cadena = cadena + str(cadenaTemporal[2])
				if(cadenaTemporal[5]!="*" ):
					cadena = cadena + cadenaTemporal[5]
				if(cadenaTemporal[6]!="*" ):
					cadena = cadena + cadenaTemporal[6]
				if(cadena.count("1")%2==0):
					cadenaTemporal[1]= "0"
				else:
						cadenaTemporal[1]= "1"	
			if(i==3):
				if(cadenaTemporal[4]!="*" ):
					cadena = cadena + cadenaTemporal[4]
				if(cadenaTemporal[5]!="*" ):
					cadena = cadena + cadenaTemporal[5]
				if(cadenaTemporal[6]!="*" ):
					cadena = cadena + cadenaTemporal[6]
				if(cadena.count("1")%2==0):
					cadenaTemporal[3]= "0"
				else:
					cadenaTemporal[3]= "1"		
			cadena = ''
			i = i+1;			

		j=j+1
	'''fila= cadena.count("*")
	cadenaTemporal = []
	i=0;
	while (fila>i):
		salto = 2**(i)
		for j in range(len(cadenaAuto)):
			if (j%2==0 and cadenaAuto[j]!="*"):
				cadenaTemporal = cadenaTemporal + cadenaAuto[j]
			salto = salto+
		i=i+1'''



mensaje = "1000110101011101"
listaPalabras = palabras(4,mensaje)
paridad(agrRedundancia(listaPalabras,3))
print(listaPalabras)
