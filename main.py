def bubble_sort(lista): 
    n = len(lista)
    for i in range(n):
        for j in range (0,n - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

numeros = [5,1,4,2,3,4,56,78,2,78,34,23,98,4,]
print("bubble sorted:", bubble_sort(numeros)) # prueba de comment

def insertion_sort(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

numero = [5,1,4,2,3,4,56,78,2,78,34,23,98,4]
print(insertion_sort(numero))

def busqueda_binaria(lista_ordenada, objeto):
    izquierda = 0
    derecha = len(lista_ordenada) - 1
    while izquierda <= derecha: 
        medio = (izquierda + derecha) // 2
        
        if lista_ordenada[medio] == objeto:
            return medio
        elif lista_ordenada[medio] < objeto:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

datos = [1, 2, 3, 45, 50]
resultado = busqueda_binaria(datos, 45)
print(f"el elemento encontrado en el indice: {resultado}")

# casting de tipos de datos 
#int()
#float()
#str()
#bool()
#list() -> (map/filter)
#tuple()
#dict()

precio_texto = "49,99"
print("Texto original", precio_texto, type(precio_texto))
precio_decimal = float(precio_texto.replace(",","."))
# no acepta comas , asi que se transforma con el .replace la , por el punto
print("el texto se convirtió en:",precio_decimal, type(precio_decimal))

precio_entero = int(precio_decimal) # quita el decimal
print("el texto se convirtió en entero:",precio_entero, type(precio_entero))

# funciones 
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

resultado_area = calcular_area_rectangulo(5,10)
print("el area del rectangulo es:",resultado_area)
## Ó 
print("el area del rectangulo es:", calcular_area_rectangulo(5,10)) 

# alcance
impuesto_global =0.15
def calcular_precio_final(precio_base):
    descuento_local = 5.0

    precio_con_descuento = precio_base - descuento_local
    precio_final = precio_con_descuento + (precio_con_descuento * impuesto_global)
    return descuento_local

print("precio final con impuestos:", calcular_precio_final(100))

# funciones anidadas
def agregar_envio(precio):
    return precio + 5

# segunda funcion agrega al 10% del impuesto recibido
def agregar_impuestos(precio_con_envio):
    return precio_con_envio * 1.10
costo_total = agregar_impuestos(agregar_envio(50))
print("el costo total con impuestos es:", costo_total)

# funciones lamda (funciones de una linea)
# lambda es una funcion, pero más corta o de una sola linea
## ejemplo 1 
elevar_al_cuadrado = lambda x:x**2 # se guarda en un espacio de memoria
print("cuadrado de 4:", elevar_al_cuadrado(4))

# ejemplo 2
numeros = [1,2,3,4,5]
cuadrados = list(map(lambda x:x**2, numeros)) ## a cada elemento elevalo al cuadrado
print(f"el cuadrado de {numeros} es:",cuadrados)

# ejemplo 3 
nombres=["hola","que","tal"]

nombres_mayuscula = list(map(lambda palabra: palabra.upper(),nombres))
## el list() es para que el map() devuelva la lista
## el map() es para que vaya con cada elemento de la lista, lo vuelve iterable
##.upper es para cambiar a mayuscula
## lambda palabra:palabra.upper, la primera palabra es un elemento y la segunda es la transformacion, 
## nombres : es para decir el nombre de la variable 
print(f"los nombres en mayuscula para{nombres} son:", nombres_mayuscula) 