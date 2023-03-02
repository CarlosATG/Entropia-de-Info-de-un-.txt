import string
import itertools
import numpy as np
import csv

file = open('YOUR.txt', 'r')#Abrimos y leemos el archivo
data = file.read()#Guardamos esta info en una variable

Letras = string.printable #Creamos una variable con todos los caracteres ascii
LetrasUno= string.printable #Creamos la varible que vamos a usar para calcular la entropia de primer orden
TotalChar = 0.0 #Creamos la varible que contabilizará la cantidad de caracteres
ProbLetra= np.zeros(len(Letras)) #Creamos una arreglo del mismo tamaño que la cantidad de caracteres para guardar la probabilidad
ProbTotal= 0.00 #Creamos una varibale para la probabilidad, ya que la usaremos en el cálculo de la entropia
EntropiaUno = 0.00 #Creamos una varable para la entropía

for i in range (0, len(Letras)): #Para caluclar la probabilidad necesitamos saber cuantos caracteres hay
    TotalChar+=data.count(Letras[i]) #El total de caracteres será igual a la suma de la cantidad de veces que aparece cada uno

Contador=np.zeros(len(Letras)) #Creamos un arreglo que guardará cuantas veces aparece cada caracter
for i in range (0, len(Letras)):#Un ciclo para ir por todos los caracteres
    Contador[i]=data.count(Letras[i]) #El valor de la posición del ciclo será igual a la veces que aparece el caracter
    ProbLetra[i] = Contador[i] / TotalChar #La probabilidad de que aparezca el caracter es igual a sus apáriciones entre el total
    ProbTotal += ProbLetra[i] #Nos sirve para verificar la regla numeor uno de la porbabilidad, la suma de todas debe dar 1
    if ProbLetra[i]>0: #Hay errores si lan probabilidad de un caracter es 0, al momento de calcular la entropia
        informacion = np.log2(1/ProbLetra[i]) #La información se define como el logaritmo base 2 del inverso de la porbabiliadad
        EntropiaUno += ProbLetra[i] * informacion #La entropia es la suma del producto de la probabilidad del caracter por su información

#Ahora vamos a repetir el proceso, pero para dos símbolos
LetrasDos= list(itertools.combinations_with_replacement(Letras, 2))#Utilizando itertools podemos facilitar y encontrar todas las combinaciones de dos cracteres
ContadorDos=np.zeros(len(LetrasDos))#Creamos un arreglo con tantos espacios como combinaciones de dos cracteres
Lectura = LetrasDos #Igualamos la variable lectura a Letras dos, ya que más adelante tendremos que hacer operaciones osbre ella
EntropiaDos = 0.00 #Aquí estaremos sumando el valor del producto de la probailidad por infomración de cada caracter
ProbLetraDos = np.zeros(len(LetrasDos))#la probabilidad de los caracteres será guardada en un arreglo del mismo tamaño que cantidad de caracteres
CharDos = 0.00 #Aquí guardaremos la cantidad de veces que aparecen todas las combinaciones
for i in range (0, len(LetrasDos)): #Ciclo para ver cuantas veces sale cada combinación
    Lectura[i]=''.join(LetrasDos[i]) #Eliminamos espacios o comillas al momento de concatenar los dos caracteres
    ContadorDos[i]=data.count(Lectura[i])#guardamos la cantidad de veces que sale la combinación de dos simbolos en eta variable
    CharDos += data.count(Lectura[i])#Sumamos a un total para saber cuantas combinaciones de dos símbolos hay
for i in range (0, len(LetrasDos)): #Ciclo para encontrar la entropia de segundo orden
    ProbLetraDos[i] = ContadorDos[i]/CharDos #La probabilidad de que aprezca un conjunto es igual a las veces que salió entre el total de veces que hay conjuntos
    if ProbLetraDos[i]>0: #Igual que en la parte de un símbolo, hay error si tenemos simbolos con probabilidad 0
        informacion = np.log2(1 / ProbLetraDos[i])#La información se define como el logaritmo base 2 del inverso de la probabilidad
        EntropiaDos += ProbLetraDos[i] * informacion#La entropia es la suma del producto de la probabilidad del caracter por su información

#Ahora vamos a repetir el proceso para tres símbolos
LetrasTres= list(itertools.combinations_with_replacement(Letras, 3))#Utilizando itertools podemos facilitar y encontrar todas las combinaciones de dos cracteres
ContadorTres=np.zeros(len(LetrasTres))#Creamos un arreglo con tantos espacios como combinaciones de tres símbolos
LecturaTres = LetrasTres #Igualamos la variable lectura a Letras trs, ya que más adelante tendremos que hacer operaciones osbre ella
EntropiaTres = 0.00#Aquí estaremos sumando el valor del producto de la probailidad por infomración de cada caracter
ProbLetraTres = np.zeros(len(LetrasTres))#la probabilidad de los caracteres será guardada en un arreglo del mismo tamaño que cantidad de caracteres
CharTres = 0.00#Aquí guardaremos la cantidad de veces que aparecen todas las combinaciones
for i in range (0, len(LetrasTres)):#Ciclo para ver cuantas veces sale cada combinación
    LecturaTres[i]=''.join(LetrasTres[i])#Eliminamos espacios o comillas al momento de concatenar los tres símbolos
    ContadorTres[i]=data.count(LecturaTres[i])#guardamos la cantidad de veces que sale la combinación de dos simbolos en eta variable
    CharTres += ContadorTres[i]#Sumamos a un total para saber cuantas combinaciones de tres símbolos hay
for i in range (0, len(LetrasTres)):#Ciclo para encontrar la entropia de tercer orden
    ProbLetraTres[i] = ContadorTres[i]/CharTres#La probabilidad de que aprezca un conjunto es igual a las veces que salió entre el total de veces que hay conjuntos
    if ProbLetraTres[i]>0:#Igual que en la parte de un símbolo, hay error si tenemos simbolos con probabilidad 0
        informacion = np.log2(1 / ProbLetraTres[i])#La información se define como el logaritmo base 2 del inverso de la probabilidad
        EntropiaTres += ProbLetraTres[i] * informacion#La entropia es la suma del producto de la probabilidad del caracter por su información

print(f'Entropia de un simbolo = {EntropiaUno}')#Obtenemos la entropia uno en terminal
print(f'Entropia de Dos simbolos seguidos = {EntropiaDos} = {2*EntropiaUno}')#Obtenemos la entropía de segundo orden que debe ser igual a 2 veces la de primer orden
print(f'Entropia de Tres simbolos seguidos = { EntropiaTres} = {3* EntropiaUno}')#Obtenemos la entropía de tercer orden que debe ser igual a 3 veces la de primer orden
with open('Nombre.csv', 'w') as file:#guardamos infomración en un escel
    writer = csv.writer(file)
    writer.writerow(Letras)#simbolos
    writer.writerow(Contador)#Veces que aparece
    writer.writerow(ProbLetra)#Su probabilidad
#print(np.sum(ProbLetra))
#print(np.sum(ProbLetraDos))
#print(np.sum(ProbLetraTres))
