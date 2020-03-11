

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


mensaje = ('01')

codigoM = manchester(mensaje)
print(codigoM)

deCode = desManchester(codigoM)
print(deCode)
