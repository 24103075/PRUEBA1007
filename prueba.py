
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}


def stock_marca(marca):
    for codigo,datos in productos.items(): 
        if datos [0].lower() == marca.lower():
            marca=productos[codigo][0]
            cantidad=stock[codigo][1]
        print("Marca:",marca)
        print("Cantidad:",cantidad)
        return


def busqueda_precio(p_min, p_max):
        resultado=[]
        
        for codigo,datos in stock.items():
          precio=datos[0]
          if precio >= p_min and precio <= p_max and stock[codigo][0]  > 0 :
           resultado.append(codigo+"--"+ productos[codigo][0])

        if resultado:
           resultado.sort()
           print("Producto :",resultado)
        
        else:
            print("No hay notebooks para este rango de precios")


def actualizar_precio(modelo, p):
     
     if modelo in stock:
       stock[modelo][1]=p
       return True
     return False

     
     

         
         
        
            
def main ():
    
    while True:

       print("*** MENU PRINCIPAL ***")
       print("1.Stock marca")
       print("2.Busqueda por precio")
       print("3. Actualizar precio")
       print("4. Salir")

       try:
         opc=int(input("Ingrese una opcion de (1 a 5):"))
       except ValueError:
         print("Puede ingresar solo valores numericos")#
        
       if opc == 1:
          marca=input("Ingrese la marca que desea consultar:")
          stock_marca(marca)
                 
       elif opc == 2:
            while True:
                try:
                 p_min=int(input("Ingrese precio minimo:"))
                 p_max=int(input("Ingrese el precio maximo:"))
                 busqueda_precio(p_min, p_max)
                except ValueError:
                    print("Debe ingresar valores enteros!!")
                
                break
       elif opc == 3:
             
             codigo=input("Ingrese el codigo del producto:")
             try:
                nuevo_valor=int(input("Ingrese el nuevo valor:"))
                if actualizar_precio(modelo, p):
                    print("Precio actualizado")
                else:
                    print("Codigo no existe ")
             except ValueError:
                 print("Puede ingresar solo valores numericos ")
             nva_consulta=input("Desea actuaizar otro producto (s=si/n=no)?:").lower()
             if nva_consulta =="n":
                 break
                 

             
       elif opc == 4:
            print("Programa finalizado")
            break
       else:
            print("Debe seleccionar una opcion valida!!")



if __name__ == "__main__":
    main()