#Williams_Rodriguez_005D_D

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
                      '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
                      'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
                     'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
                     'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
                     '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
                     '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
                     'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
              'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
              'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],}
def stock_marca(marca):
    total = 0
    for modelo, datos in productos.items():
        if datos[0].lower() == marca.lower():
            total += stock[modelo][1]
    print(f"El stock de la mara  es: {total}")


def busqueda_precio(ram_minimo, ram_maximo,precio_minimo, preico_maximo):
    resultado = []
    for modelo, datos in stock.items():
        precio, cantidad = datos
        if precio_minimo <= precio <= preico_maximo and cantidad > 0:
            marca = productos[modelo][0]
            resultado.append(f"{marca}--{modelo}")
        if ram_minimo <= precio <= ram_maximo and cantidad > 0:
            marca = productos[modelo][0]
            resultado.append(f"{marca}--{modelo}")
    if resultado:
        print("Los notebooks entre los precios consultas son:", sorted(resultado))
    else:
        print("No hay notebooks en ese rango de precios.")
def eliminar_prodducto (modelo):
  if modelo in productos and modelo in stock:
        del productos[modelo]
        del stock[modelo]
  else:
      False


def menu():
 while True:
    print("---------------------------")
    print("---Menu Principal---")
    print("1.stock de la marca. ")
    print("2.Busqueda por RAM y precio. ")
    print("3.Eliminar producto. ")
    print("4.Salir")
    print("--------------------------")
    opcion =input("indique una opcion: ")

    if opcion =="1":
        marca = input("ingrese la marca a consultar: ")
        stock_marca(marca)
    elif opcion == '2':
            while True:
                try:
                    precio_minimo = int(input("Ingrese precio mínimo: "))
                    precio_maximo = int(input("Ingrese precio máximo: "))
                    ram_minima= int(input("Ingrese La ram Minima: "))
                    ram_maxima = int(input("Ingrese la ram maxima"))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
            busqueda_precio(precio_minimo, precio_maximo,ram_maxima,ram_minima)
    elif opcion == '3':
            while True:
                modelo = input("Ingrese modelo a eliminar: ")
                if eliminar_prodducto(modelo):
                    print("Producto eliminado!!")
                else:
                    print("El modelo no existe!!")
                seguir = input("Desea eliminar otro producto (s/n)?: ").lower()
                if seguir != 'si':
                    break

    elif opcion == '4':
            print("Programa finalizado.")
            break

    else:
       print("Debe seleccionar una opción válida!!")


    

    

menu()