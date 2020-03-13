import random
#from matplotlib import *
import time

def agrRedundancia(listaPalabras,bitRed):
	listRedundante= [];
	for i in range(len(listaPalabras)):
		palabra = listaPalabras[i]
		for j in range(bitRed):
			palabra.insert(2**j-1,"*")
		listRedundante.append(palabra)
	return listRedundante		

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


def dividirPalabras(tamaño,mensaje):
	palabras=[];
	i= 0;
	for j in range(int(len(mensaje)/tamaño)):
		palabra =mensaje[i:tamaño*(j+1)]
		palabra2 = list(palabra)
		palabras.append(palabra2)
		i=i+tamaño
	return palabras


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
		
def comproHamming(cadenaAuto):
	cadena = ''
	resultadosParidad = ''
	for j in range(len(cadenaAuto)):
		i=0
		cadenaTemporal = cadenaAuto[j]
		while(i<len(cadenaTemporal)):
			if (i==0):
				cadena = cadena + str(cadenaTemporal[0])
				cadena = cadena + str(cadenaTemporal[2])
				cadena = cadena + str(cadenaTemporal[4])
				cadena = cadena + str(cadenaTemporal[6])
				
				if(cadena.count("1")%2==0):
					resultadosParidad = resultadosParidad + str(0)
				else:
					resultadosParidad = resultadosParidad + str(1)
	
			if (i==1):
				cadena = ''
				cadena = cadena + str(cadenaTemporal[1])
				cadena = cadena + str(cadenaTemporal[2])
				cadena = cadena + str(cadenaTemporal[5])
				cadena = cadena + str(cadenaTemporal[6])
				
				if(cadena.count("1")%2==0):
					resultadosParidad = resultadosParidad + str(0)
				else:
					resultadosParidad = resultadosParidad + str(1)
			if(i==3):
				cadena = ''
				cadena = cadena + str(cadenaTemporal[3])
				cadena = cadena + str(cadenaTemporal[4])
				cadena = cadena + str(cadenaTemporal[5])
				cadena = cadena + str(cadenaTemporal[6])
				
				if(cadena.count("1")%2==0):
					resultadosParidad = resultadosParidad + str(0)
				else:
					resultadosParidad = resultadosParidad + str(1)
			cadena = ''
			i = i+1;			
		j=j+1
		if(resultadosParidad.count(0) != 3):
			posicionError = convercionDecimal (resultadosParidad)
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
	





#f = open ("manchester.txt", "r")
#mensaje = f.read()

mensaje = "1000110101011101"
listaPalabras = dividirPalabras(4,mensaje)
paridad(agrRedundancia(listaPalabras,3))
print(listaPalabras)
comproHamming(listaPalabras)
listaPalabras = dividirPalabras(7, mensaje)
#convercionDecimal('001')

