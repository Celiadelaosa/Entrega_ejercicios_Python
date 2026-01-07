#ENTREGA PYTHON --Celia de la Osa Fernández

#obs: hay un salto del ejercicio 34 al 36 (en los enunciados no aparece el 35)

# ============================
# EJERCICIO 1
# ============================
#1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con 
# las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
def frecuencias_letras(texto):   #definimos la función
    texto=texto.lower()          #pasamos todo el texto a minúsculas para que no tome como letras diferentes una mayúscula y una minúscula
    frecuencias={}               #creamos un diccionario vacío en el que recogeremos las letras y sus frecuencias
    for letra in texto:          #recorremos la cadena de texto
        if letra!=' ':           #y solo se ejecuta el código siguiente si tenemos una letra (no tenemos en cuenta los espacios)
            if letra in frecuencias:    #si la letra ya está en el diccionario que hemos creado (tomamos las letras como keys en el diccionario)
                frecuencias[letra]+=1   #le sumamos uno a su 'value' correspondiente (ya que significa que está repetida)
            else:                       #si esa letra aún no está en nuestro diccionario 
                frecuencias[letra]=1    #le conferimos el value 1 (al darle un valor la estamos añadiendo como key en el diccionario)
    return(frecuencias)               #la función nos devuelve el diccionario


#comprobamos que la función funciona 
#si usáramos un print nos devolvería el diccionario en una sola línea, lo que creo que es menos visual a la hora de saber cuántas letras hay de cada
frecuencias_letras('Hola a todos')

# ============================
# EJERCICIO 2
# ============================
#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

#comenzamos creando una función que nos devuelva el doble de un número
def duplicar(numero):
    return 2*numero

#usamos map para aplicar la función que acabamos de crear a una lista de números
lista_numeros=[1,2,3,4,5,12,15,17] #damos una lista en la que usaremos la función 
resultado=list(map(duplicar,lista_numeros)) #hago un list de la función map porque map por sí solo no me "devuelve nada"
print(resultado)


# ============================
# EJERCICIO 3
# ============================
#3.  Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe 
#devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def cuenta_palabras(lista, palabra_objetivo):
    contador=0
    palabra_objetivo=palabra_objetivo.lower()
    for palabra in lista:
        palabra=palabra.lower()
        if palabra==palabra_objetivo:
            contador+=1
        else:
            continue
    return f'El número de veces que aparece la palabra objetivo es {contador}' #inicialmente había usado print, pero con return podríamos reutilizar la info (el return no solo imprime como print)

#probamos que funciona
cuenta_palabras(['NAVIDAD', 'navidad', 'roscón', 'luces', 'polvorón'], 'navidad')


# ============================
# EJERCICIO 4
# ============================
#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función 
#map()

#comenzamos creando una función que reste valores
def resta(a,b):
    return a-b

lista_1=[0,1,2,4,5,6,14] #proporcionamos dos listas 
lista_2=[1,2,3,7,8,8,9]
if len(lista_1)!=len(lista_2):              #si las listas no tienen la misma longitud generamos un mensaje
    print ('Las listas no tienen la misma longitud')
else:                                  #en otro caso queremos que nos devuelva el resultado de la resta
    print(list(map(resta,lista_1, lista_2)))  



# ============================
# EJERCICIO 5
# ============================
#5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por 
#defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor 
# o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". 
# La función debe devolver una tupla que contenga la media y el estado.

#he investigado y, si importo un módulo concreto, hay funciones integradas que calculan la media
#aquí lo hago "manualmente"
def calculadora_media(lista_notas, nota_aprobado=5):     #tomamos 5 como el valor predeterminado para aprobar
    media=sum(lista_notas)/len(lista_notas)        #calculamos la media
    if media>= nota_aprobado:          #si la media es mayor o igual a 5 devuelve la media y aprobado
        return (media, 'aprobado') #usamos return como buena práctica
    else:                                 #en otro caso devuelve la media y "suspenso"
        return (media, 'suspenso')  

#la probamos
calculadora_media([2,3.7,10,6,7,8])


# ============================
# EJERCICIO 6
# ============================
#6. Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(numero):       #definimos la función donde el parámetro es un número
    if numero<=0:            #evitamso los casos donde el número no es positivo
        print ('El número debe ser positivo')
    else:
        anterior=numero-1        #llamamos anterior al valor anterior a nuestro número
        if numero==1:            #si el número que tenemos es 1 directamente, devolvemos 1
            return 1
        else:                    #si no...
            resultado=numero*factorial(anterior)  #usamos recursividad
        return resultado        #queremos que nos devuelva el resultado final

#comentario personal sobre la recursividad: he tenido dificultades en entender bien cómo escribirlo
#al escribirlo en papel he entendido que es como si tuviera cada factorial "expresado" y una vez llego al
#1 factorial(1)=1 y va "hacia atrás" calculando el factorial(2) a partir de factorial(1), factorial(3) 
#a partir de factorial(2) y así sucesivamente

#probamos la función
factorial(5)

# ============================
# EJERCICIO 7
# ============================
#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función 
#map()
def tupla_a_string(tupla): #el parámtero de la función será una tupla
    texto=str(tupla)       #usamos la función de string en nuestra tupla
    return(texto)   #nuestra función devuelve la cadena de texto y el tipo de elemento que es (para asegurarnos de que es un string)

#la probamos
lista_tuplas=[(1,2,3,4,5), (6,7,8), (0,1,4)]
resultado=list(map(tupla_a_string,lista_tuplas))
print(resultado)


# ============================
# EJERCICIO 8
# ============================
#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no 
# numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un 
# mensaje indicando si la división fue exitosa o no.
try:                                      #si los valores son correctos el programa debe hacer lo siguiente
    a=int(input('Escribe el dividendo'))  #como input devuelve una cadena de texto siempre, lo convertimos a número con int
    b=int(input('Escribe el divisor'))
    print(f'La operación es válida y vale {a/b}.')
except ValueError:                     #aclaramos las excepciones. Si el valor introducido por el usuario no es correcto (p.ej es una letra)
    print('Operación no válida. Debes introducir un número.')  #imprimimos este mensaje
except ZeroDivisionError:            #si el usuario proporciona un 0 como divisor
    print('Operación no válida. No se puede dividir por cero.')  #imprimimos este mensaje


# ============================
# EJERCICIO 9
# ============================
#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista 
#excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", 
#"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función 
#filter()
animales_prohibidos=['Mapache', 'Tigre', 'Serpiente Pitón', 'Cocodrilo', 'Oso']
def filtrado_animales(animal):     #sé que la propia función acepta un animal, no una lista de animales
    return animal not in animales_prohibidos

#la probamos
lista_1_animales=['Gato', 'Perro', 'Mapache', 'Serpiente Pitón', 'Vaca','Tortuga', 'Camaleón']

resultado=list(filter(filtrado_animales, lista_1_animales))
resultado


# ============================
# EJERCICIO 10
# ============================
#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una 
#excepción personalizada y maneja el error adecuadamente.

#con excepción personalizada
#comienzo dándole un nombre concreto al error 
class ListaVacia(Exception):
    pass

#manejamos el error usando try except
def calculo_promedio_2(lista_numeros):
    if len(lista_numeros)==0:
        raise ListaVacia
    return sum(lista_numeros)/len(lista_numeros)

try:
    print(calculo_promedio_2([]))
except ListaVacia:
    print('La lista está vacía')

# ============================
# EJERCICIO 11
# ============================
#11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un 
#valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones 
#adecuadamente.
try:
    edad=int(input('Introduce tu edad'))
    if edad<0 or edad>120:
        print ('La edad debe ser mayor que 0 y menor que 120.')
except ValueError:
    print('La edad debe ser un dato numérico')


# ============================
# EJERCICIO 12
# ============================
#12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
def longitud(frase):
    palabras=frase.split() #con la función split python toma los separadores (en este caso espacios) y separa cada valor (palabras) entre los mismos
    resultado=list(map(len, palabras))  #usamos map para aplicar la función len a cada palabra de nuestra lista y list para que nos lo devuelva en formato lista
    return(resultado) 

#la probamos
longitud('Hola me llamo Celia y tengo 70 años')


# ============================
# EJERCICIO 13
# ============================
#13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en 
#mayúsculas y minúsculas. Las letras no pueden estar repetidas.Usa la función 
#map()
def paso_a_tupla(caracter):                   #defino una función que,al recibir una letra, devuelve una tupla con la letra en mayúscula y minúscula
    return(caracter.lower(), caracter.upper())

def min_may(conjunto_caracteres):  #se supone que el conjunto_caracteres es de tipo set
    lista=[]   #creo una lista vacía donde almacenaré las letras en minúsculas
    for caracter in conjunto_caracteres: #para cada letra de mi lista
        caracter=caracter.lower()   #paso la letra a minúscula
        lista.append(caracter)      #añado la letra a mi lista vacía
    letras_unicas=set(lista)       #tengo una lista que he rellenado con las letras en minúscula de mi conjunto. Convierto esa lista en un set paera evitar valores duplicados
    resultado=list(map(paso_a_tupla,letras_unicas))  #uso la función de tuplas para cada caracter de mi set
    return(resultado)

#la probamos
min_may({'A', 'B', 'C', 'D', 'E', 'a','b','c','d','e'})


#intento simplificar el código anterior
def min_may_v2(conjunto_caracteres):  
    letras_unicas_v2=set([caracter.lower() for caracter in conjunto_caracteres])  #uso list comprehension y llo convierto en set de nuevo para evitar duplicados
    resultado=list(map(paso_a_tupla,letras_unicas_v2))  #uso la función de tuplas para cada caracter de mi set
    return(resultado)

#la probamos
min_may_v2({'A', 'B', 'C', 'D', 'E', 'a','b','c','d','e'})


# ============================
# EJERCICIO 14
# ============================
#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la 
#función filter()
lista_palabras=['pato', 'POLVORÓN', 'pesca', 'tomate', 'casa', 'pepe']

def filtrado_inicial(palabra, inicial='p'):  #esta función devuelve true si la palabra empiezan por p (podremos cambiar esta inicial según la que nos interese mirar) 
    return(palabra.lower().startswith(inicial))   #usamos startswith(inicial)
resultado=list(filter(filtrado_inicial, lista_palabras)) #usamos filter con nuestra función (que es booleana) y con un iterable
print(resultado)

# ============================
# EJERCICIO 15
# ============================
#15. Crea una función lambda que  sume 3 a cada número de una lista dada.
mas_tres= lambda x: x+3    #usamos la sintaxis de las funciones lambda. Nuestro parámetro es la x 
resultado=mas_tres(8)      #así podríamos reutilizar el código
print(resultado)         #comprombamos con un print


# ============================
# EJERCICIO 16
# ============================
#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de 
#todas las palabras que sean más largas que n. Usa la función filter()
 #esta función lambda nos devuelve true si las palabras son más largas que n=12 y false en caso contrario
def palabras_largas(texto, n): 
    palabras=texto.split()              #convierto el texto en una lista con sus palabras para tener una lista con las mismas (iterable) y poder usarlo con la función filter
    resultado=filter(lambda palabra:len(palabra)>n, palabras)       #usamos una función lambda booleana dentro del filter y lo aplicamos a la lista de palabras que acabamos de crear
    return(list(resultado))

#la probamos
palabras_largas('hace mucho sol en Escandinavia', 2)


# ============================
# EJERCICIO 17
# ============================
#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, 5,7,2 
#corresponde al número quinientos setenta y dos 572. Usa la función reduce()
from functools import reduce #comenzamos importando la función reduce
def cifras_a_numero(lista):      #nuestra función recibe una lista de números como parámetro
    return reduce(lambda acumulado, actual: acumulado*10+actual, lista)   #en reduce usamos una función como parámetro (¿qué hace?: toma dos valores. Para [1,2,3]: En la primera vez-> acumulado:0 actual:1; en la segunda vez acumulado 1 actual 2...

#la probamos
cifras_a_numero([1,2,3])

# ============================
# EJERCICIO 18
# ============================
#18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes 
#(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 
#90. Usa la función  filter()

#nota: he ido escribiendo el programa por fragmentos comprobando cada uno y ahora lo escribo junto
#le pedimos al usuario que nos proporcione datos para tres diccionarios y metemos esos diccionarios en una lista
lista_diccionarios=[]
for i in range(1,4):
    diccionario_i=dict(nombre=input('escribe el nombre del estudiante'), edad=int(input('escribe la edad del estudiante')), calificación=int(input('escribe la calificación')))
    lista_diccionarios.append(diccionario_i)

#usamos filter directamente sobre nuestros diccionarios, 'filtrando' a partir de la clave de calificación
resultado=list(filter(lambda diccionario: diccionario.get('calificación')>=90, lista_diccionarios))
print(resultado) #nos devuelve el diccionario completo que cumpla la condición

# ============================
# EJERCICIO 19
# ============================
#19. Crea una función lambda que filtre los números impares de una lista dada.
#pasos previos
impar=lambda x: x%2!=0    #creamos una función lambda que devuelve true si el número es impar

#lista_numeros=[1,4,5,6,45,42323,89]
#resultado=list(filter(impar,lista_numeros))     #también podríamos evitar el darle el nombre impar y ponerlo aquí directamente
#print(resultado)

#creamos ahora una función lambda que recoja todo lo anterior
filtrado_impares=lambda lista: list(filter(impar,lista))
resultado=filtrado_impares([1,2,3,4,5,6,7,8])
print(resultado)



# ============================
# EJERCICIO 20
# ============================
#20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()
lista=[1,2,'hola', 'croqueta', 50, 49, 'cielo']
resul=list(filter(lambda x: type(x)==int,lista))  #de primeras he creado la función booleana aparte y luego la he integrado en el filter
print(resul)



# ============================
# EJERCICIO 21
# ============================
#21. Crea una función que calcule el cubo de un número dado mediante una función lambda
cubo=lambda x: x**3
print(cubo (3)) #la probamos


# ============================
# EJERCICIO 22
# ============================
#22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce()
from functools import reduce
lista=[1,2,3,4,5]
producto_total=reduce(lambda x,y:x*y, lista)   #definimos una función lambda que recoja el prodcuto de dos números
print(producto_total)



# ============================
# EJERCICIO 23
# ============================
#23. Concatena una lista de palabras.Usa la función reduce()
from functools import reduce
lista_palabras=['Feliz','Navidad', 'para', 'todos']
concatena=reduce(lambda anterior,actual:anterior+' '+actual, lista_palabras)  #la idea es parecida a la del ej 17 salvo que ahora debemos concatenar palabras. Como podemos usar la función suma con strings...
print(concatena)


# ============================
# EJERCICIO 24
# ============================
#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce()
from functools import reduce
lista=[1,2,3,4,5]
diferencia_total=reduce(lambda x,y:x-y, lista)   #definimos una función lambda que recoja la función resta de dos números
print(diferencia_total)



# ============================
# EJERCICIO 25
# ============================
#25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
 #aquí contamos el espacio como caracter
def cuenta_caracteres(texto):
    return(len(texto))          

#aquí no contamos el espacio como caracter
def cuenta_caracteres_2(texto):
    return(len(texto.replace(' ','')))            #'eliminamos' los espacios con replace y miramos la nueva longitud (el número de caracteres)


# ============================
# EJERCICIO 26
# ============================
#26. Crea una función lambda que calcule el resto de la división entre dos números dados.
resto=lambda x,y: x%y        #con % hacemos el módulo (o el resto de dividir)
print(resto (117,2))         #la probamos


# ============================
# EJERCICIO 27
# ============================
#27. Crea una función que calcule el promedio de una lista de números.

#es casi igual al ejercicio 10
promedio_lista=lambda lista: sum(lista)/len(lista)     #podemos simpplificar con una función lambda
print(promedio_lista([2,3,4,5]))


# ============================
# EJERCICIO 28
# ============================
#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def primer_duplicado(lista):
    lista_2=[]                         #creamos una lista vacía
    for elemento in lista:             #recorro mi lista dada
        if elemento not in lista_2:    #si el elemento de la lista no esá en la lista (lo que ocurre si todavía no lo he añadido)
            lista_2.append(elemento)   #lo añado
        else:                          #si no, es decir, si mi elemento ya está en la lsita_2, es decir, ya lo he añadido (significa que está repetido)
            break                      #y rompo el bucle (salgo de él). Esto se lo pido porque solo quiero el primer elemento duplicado
    if len(lista)!=len(lista_2):       #de momento la función no devuelve nada. Ahora le digo que si las dos listas tienen diferente longitud me devuelva el elemento (como hemos hecho break será el primer duplicado)
        return (elemento)
    else:             #si tienen la misma longitud, que devuelva none (no mostrará nada a no ser que hagamos un print)
        return None


# ============================
# EJERCICIO 29
# ============================
#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el 
#carácter '#', excepto los últimos cuatro.
def mascara(variable):
    texto=str(variable)      #convertimos a cadena de texto
    if len(texto)<4:         #si la variable es más corta de 4 letras
        return texto         #la devuelve igual
    else:                    #si no
        dato=len(texto)-4    #como usamos esta cantidad en las dos siguientes líneas le doy un nombre para que se vea más limpio
        ultimas_4_letras=texto[dato:]     #sacamos los cuatro últimos caracteres (vamos del índice len(texto)-4 al final de la palabra)
        return((dato*'#'+ultimas_4_letras)) #devuelve tantos hastags como letras tenga la palabra (sin contar las 4 últimas letras) y las cuatro letras últimas
    


# ============================
# EJERCICIO 30
# ============================
#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras 
#pero en diferente orden.

#IDEA: CREAR TUPLAS LETRA, NUMERO DE VECES QUE APARECE Y HACER CONJUNTOS DE ESO PARA LUEGO COMPARAR LAS DUPLAS

#en el primer ejercicio ya creamos una función que creaba un diccionario donde aparecían las letras de una palabra y su frecuencia
#voy a usar esa función y a convertir los pares clave-valor en tuplas

#OBSERVACIÓN: Esta iba a ser la versión definitiva, pero después me di cuenta de que, como la función frecuencias me daba dos diccionarios podía simplificarlo (ver versión 2 justo debajo de este código)

def anagrama(palabra_1, palabra_2):
    letras_frecuencias_1=frecuencias_letras(palabra_1)  #uso la función del ejercicio 1 para conocer las letras y frecuencias de cada palabrad el input
    letras_frecuencias_2=frecuencias_letras(palabra_2)
    lista_1=[]     #creo dos listas vacías en las que meteré los pares letra:frecuencia
    lista_2=[]
    for elemento_1 in letras_frecuencias_1.items():
        lista_1+=tuple(elemento_1)        #añado las duplas a mis listas
    for elemento_2 in letras_frecuencias_2.items():
        lista_2+=tuple(elemento_2)
    if set(lista_1)==set(lista_2):        #convierto las listas en conjuntos para no tener en cuenta el orden (si no, ningún par de palabras sería un anagrama)
        print(f'La palabra {palabra_1} y la palabra {palabra_2} son anagramas')
    else:
        print(f'La palabra {palabra_1} y la palabra {palabra_2}  NO son anagramas')

#la probamos
anagrama('flauta', 'flaut')  #con la primera función que había creado, estas palabras (al tener las mismas letras) daban el output de ser anagramas. Con esta nueva función da un resultado correcto 
anagrama('roma', 'amor')

#VERSIÓN 2 (MUCHO MÁS SIMPLE)

def anagrama2(palabra_1, palabra_2):
    if frecuencias_letras(palabra_1)==frecuencias_letras(palabra_2):
        print(f'La palabra {palabra_1} y la palabra {palabra_2} son anagramas.')
    else:
        print(f'La palabra {palabra_1} y la palabra {palabra_2} NO son anagramas.')

#la probamos
anagrama2('flauta', 'flaut')  
anagrama2('roma', 'amor')

# ============================
# EJERCICIO 31
# ============================
#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en 
#esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se 
#lanza una excepción.
def encuentra_nombre():
    lista_nombres=input('Dame nombres separados por espacios y escritos en minúsculas').split() #con split obtenemos una lista
    nombre=input('¿Qué nombre quieres que encuentre?')
    if nombre not in lista_nombres:
        raise ValueError(f'El nombre {nombre.capitalize()} NO está en la lista')
    return(f'El nombre {nombre.capitalize()} está en la lista')
#la probamos
encuentra_nombre()


# ============================
# EJERCICIO 32
# ============================
#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y 
#devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona 
#no trabaja aquí.
def encuentra_empleado(nombre, empleados):    #empleados es un diccionario
    if nombre in empleados.keys():
        print(f'El puesto de {nombre} es {empleados[nombre]}.')
    else:
        print(f'La persona {nombre} no trabaja aquí.')
#la probamos
empleados = {
    'Ana Pérez': 'Analista de datos',
    'Luis Gómez': 'Desarrollador',
    'María López': 'Recursos Humanos'
}
nombre='Ana Pérez'
encuentra_empleado(nombre, empleados)



# ============================
# EJERCICIO 33
# ============================
#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

#como queremos emparejar los elementos usamos la función zip
suma_listas= lambda lista_1, lista_2: [x+y for x,y in zip(lista_1, lista_2)]   #lo convertimos en lista porque si no el for da error 
print(suma_listas([1,2,3], [4,5,6]))


# ============================
# EJERCICIO 34
# ============================
#34. 
#Crea la clase 
#Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: 
#crecer_tronco , 
#nueva_rama , 
#crecer_ramas , 
#quitar_rama e 
#info_arbol . El objetivo es implementar estos métodos para 
#manipular la estructura del árbol.

#Código a seguir:
#1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#2. Implementar el método 
#crecer_tronco para aumentar la longitud del tronco en una unidad.
#3. Implementar el método 
#nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#4. Implementar el método 
#crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#5. Implementar el método 
#quitar_rama para eliminar una rama en una posición específica.
#6. Implementar el método 
#info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las 
#mismas.

#Caso de uso:
#1. Crear un árbol.
#2. Hacer crecer el tronco del árbol una unidad.
#3. Añadir una nueva rama al árbol.
#4. Hacer crecer todas las ramas del árbol una unidad.
#5. Añadir dos nuevas ramas al árbol.
#6. Retirar la rama situada en la posición 2.
#7. Obtener información sobre el árbol.

class Arbol:
    def __init__(self):
        self.tronco = 1     #empezamos con la longitud del tronco igual a 1 y una lista vacía de ramas
        self.ramas = []

    def crecer_tronco(self): #definimos el primer método
        self.tronco += 1     #que le suma 1 a la longitud del tronco
        print(f'Se ha añadido una unidad de longitud al tronco.')
    
    def nueva_rama(self):
        self.ramas.append(1)
        print(f'Se ha añadido una rama.')
    
    def crecer_ramas(self):
        for i in range(len(self.ramas)):       #recorremos las posiciones de los elementos en la lista de ramas
            self.ramas[i]+=1                   #para cada valor de esa lisat (al que accedemos con la posición que ocupa) le sumamos 1

    def quitar_rama(self, posicion_especifica):
        self.ramas.pop(posicion_especifica)    #eliminamos un solo elemento de la lista de ramas, el que está en la posición concreta
        print('Hemos quitado una rama.')
    
    def info_arbol(self):
        print(f'La longitud del tronco es {self.tronco}.')
        print(f'El número de ramas es {len(self.ramas)}.')
        print(f'Las longitudes de las ramas son {self.ramas}.')

# 1. Creamos un árbol
olmo = Arbol()

# 2. Crecer el tronco
olmo.crecer_tronco()

# 3. Añadir una nueva rama
olmo.nueva_rama()

# 4. Crecer todas las ramas
olmo.crecer_ramas()

# 5. Añadir dos nuevas ramas
olmo.nueva_rama()
olmo.nueva_rama()

# 6. Quitar la rama en la posición 2
olmo.quitar_rama(2)   #es posición 2, rama 3

# 7. Mostrar la información del árbol
olmo.info_arbol()


# ============================
# EJERCICIO 35
# ============================

#Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta 
#corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y 
#agregar dinero al saldo.
#Código a seguir:
#a) Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False
#b) implementar el método  retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
#c)Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
#d)Implementar el método agregar_dinero para agregar dinero al saldo del usuario.

#Caso de uso:
#a)Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
#b)Agregar 20 unidades de saldo de "Bob".
#c)Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
#d)Retirar 50 unidades de saldo a "Alicia".
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre=nombre
        self.saldo=saldo
        self.cuenta_corriente=cuenta_corriente

    def retirar_dinero(self, dinero_a_retirar):
        if self.saldo>=dinero_a_retirar:
            self.saldo-=dinero_a_retirar
            print(f'Se han retirado {dinero_a_retirar} unidades de saldo de la cuenta de {self.nombre}. El saldo actual es de {self.saldo} unidades.')
        else:
            print('El saldo de la cuenta bancaria no es suficiente')
    
    def transferir_dinero(self,usuario_donante, cantidad_a_transferir):
        if usuario_donante.saldo>=cantidad_a_transferir:
            self.saldo+=cantidad_a_transferir   #añadimos el dinero a la cuenta destino
            usuario_donante.saldo-=cantidad_a_transferir #pero también debemos sustraer la cantidad de la cuenta origen (esto, en un principio, pasó desapercibido para mí)
            print(f'{usuario_donante.nombre} ha realizado una transferencia por valor de {cantidad_a_transferir} unidades de saldo a {self.nombre}. El saldo actual de {self.nombre} es {self.saldo}.')
        else:
            print(f'{usuario_donante.nombre} no tiene suficiente dinero en la cuenta para transferir {cantidad_a_transferir} unidades de saldo a {self.nombre}.')

    def agregar_dinero(self, dinero_a_añadir):
        self.saldo+=dinero_a_añadir
        print(f'Se han agregado {dinero_a_añadir} unidades de saldo a la cuenta de {self.nombre}. El saldo actual es de {self.saldo}.')



Alicia=UsuarioBanco('Alicia', 100, True)
Bob=UsuarioBanco('Bob', 50, True)

Bob.agregar_dinero(20)
Bob.transferir_dinero(Alicia, 80)   # 'el self es la cuenta destino'
Alicia.retirar_dinero(Alicia, 50)



# ============================
# EJERCICIO 36
# ============================
#37. Crea una función llamada 
#procesar_texto que procesa un texto según la opción especificada: 
#reemplazar_palabras , 
#procesar_texto .
#contar_palabras , 
#eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función 

#Código a seguir:
#1.Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
#2.Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva. Tiene que devolver el texto con el remplazo de palabras.
#3.Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra #eliminada.
#4.Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un 
#número de argumentos variable según la opción indicada.

#Caso de uso:
#Comprueba el funcionamiento completo de la función 
#procesar_texto

#esta función es análoga a la del primer ejercicio
def contar_palabras(texto):
    frecuencia_palabras={}    #creamos un diccionario vacío en el que incluiremos las palabras y sus frecuencias
    palabras_texto=texto.split()   #en esta ocasión usamos el split para evitar los espacios
    for palabra in palabras_texto:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra]+=1
        else:
            frecuencia_palabras[palabra]=1
        
    return frecuencia_palabras

def reemplazar_palabra(texto,palabra_a_reemplazar, palabra_nueva):
    if palabra_a_reemplazar in texto:
        nuevo_texto=texto.replace(palabra_a_reemplazar, palabra_nueva)    #le doy un nombre porque si no me devuelve el mismo texto (replace no guarda la nueva cadena de por sí)
        return nuevo_texto
    else: 
        return texto

def eliminar_palabra(texto, palabra_a_eliminar):
    a_eliminar=palabra_a_eliminar+' '   #añdimos un espacio para que en el texto que devuelva no parezca que hemos quitado una palabra
    nuevo_texto=texto.replace(a_eliminar,'')  #usamos replace donde la palabra nueva no es nada
    return nuevo_texto



def procesar_texto(texto, opcion, *args): #como queremos un argumento variables usamos *args
    if opcion=='contar':
        return contar_palabras(texto)
    
    elif opcion=='reemplazar':
        palabra_a_reemplazar, palabra_nueva =args #definimos los argumentos para esta función
        return reemplazar_palabra(texto, palabra_a_reemplazar, palabra_nueva)
    
    elif opcion=='eliminar':
        palabra_a_eliminar=args[0]         #aquí debemos incluir [0] para que no dé error. *args es una tupla pero en este caso solo quiero incluir un elemento, así que tengo que escribir la posición. En el caso de replace es diferente porque ya tengo dos argumentos
        return eliminar_palabra(texto, palabra_a_eliminar)
    
    else:
        print('La opción escogida no es factible.')
    


#lo comprobamos
texto='Hola me llamo Antonia y me encanta el salchichón.'
print(procesar_texto(texto, 'contar'))
print(procesar_texto(texto, 'reemplazar', 'Antonia', 'Mercedes'))
print(procesar_texto(texto, 'eliminar', 'Hola'))



# ============================
# EJERCICIO 37
# ============================
# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
hora=input('¿Qué hora es?')
hora_min=hora.split(':')    #daremos la hora en formato hora:minutos,como quremos fijarnos solo en al hora, lo separamos
if int(hora_min[0])>23 or int(hora_min[0])<0 or int(hora_min[1])>59 or int(hora_min[1])<0:       #incluimos el int (lo convertimos a número) para poder usar los símbolos de comparación
    print('Introduce una hora válida.')
elif 0<=int(hora_min[0])<12:                   #consideramos horas diurnas entre las 0:00-11:59
    print ('Es de día.')
elif 12<=int(hora_min[0])<=18:                 #consideramos horas de por la tarde entre las 12:00-18:59
    print('Es por la tarde.')
elif 18<int(hora_min[0])<=23:                  #consideramos horas de noche netre las 19:00-23:59
    print('Es de noche.')


# ============================
# EJERCICIO 38
# ============================
#39.  Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. 
#Las reglas de calificación son:
#0 - 69 insuficiente
#70 - 79 bien
#80 - 89 muy bien
#90 - 100 excelente

nota_numerica=int(input('¿Qué nota tiene el alumno?'))
if 0<=nota_numerica<=69:
    print ('Insuficiente')
elif 70<=nota_numerica<=79:
    print ('Bien')
elif 80<=nota_numerica<=89:
    print ('Muy bien')
elif 90<=nota_numerica<=100:
    print ('Excelente')
else:
    print('Introduce una nota válida')



# ============================
# EJERCICIO 39
# ============================
#40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "triangulo" "rectangulo" o "circulo") y 
#datos (una tupla con los datos necesarios para calcular el área de la figura).

#importamos el número pi para el área del círculo
import math

print(math.pi)

def area_figura(figura, datos):            #datos es la tupla
    if figura=='triángulo':
        base,altura=datos
        return(f'El área del triángulo es {base*altura/2}.')
    elif figura=='rectángulo':
        base,altura=datos
        return(f'El área del rectángulo es {base*altura}.')
    elif figura=='círculo':
        radio=datos[0]
        return(f'El área del círculo es {math.pi*(radio**2)}.')   #en el caso del cículo solo hace falta un argumento
    else:
        return ('La figura no es correcta.')

area_figura('triángulo',(6,3))
area_figura('cuadrado',(2,2))
area_figura('rectángulo',(2,5))
area_figura('círculo', (4,))



# ============================
# EJERCICIO 40
# ============================
#41.  En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el 
#monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo 
#siguiente:
#1. Solicita al usuario que ingrese el precio original de un artículo.
#2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
#3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
#4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor 
#a cero). Por ejemplo, descuento de 15€. 
#5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
#6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu 
#programa de Python.


precio=int(input('Escribe el precio del artículo'))
if precio<=0:
    print('Introduce un precio válido.')
else:
    cupon=input('¿Tienes cupón descuento?')
    if cupon=='sí':
        valor_cupon=int(input('¿Qué valor tiene tu cupón descuento?'))
        if valor_cupon<=0:
            print('Ese descuento no es válido')
        elif valor_cupon<=precio:
            print(f'Tu cupón ha sido aplicado con éxito. El precio rebajado del artículo es de {precio-valor_cupon} euros.')
        else:
            print(f'Quizás deberías aprovechar tu cupón en otro artículo. El precio de producto es menor al valor de tu cupón. Estás perdiendo {valor_cupon-precio} euros.')
    elif cupon=='no':
        print(f'El precio de tu artículo se mantiene, cuesta {precio} euros.')
    else:
        print('Debes responder sí o no a la pregunta de si tienes un cupón descuento.')










