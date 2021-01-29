from datetime import datetime
def venta():
    vendedor = input("Digite el nombre del vendedor: ")
    comprador = input("\nDigite el nombre del cliente: ")
    time = datetime.now()
    time = time.strftime("%D - %H: %M")
    productos = list()
    agregar = True
    precio_total = 0
    cantidad_total = 0
    while(agregar):
        try:
            nombre_producto = str(input("\nDigite el nombre del producto: "))
            codigo = int(input("\nDigite el codigo del producto: "))
            cantidad = int(input("\nDigite la cantidad del producto: "))
            precio = float(input("\nDigite el precio del producto: "))
            precio_venta = float((precio * cantidad))
            producto = {"nombre":nombre_producto, "codigo":codigo, "cantidad":cantidad, "precio":precio, "precio_venta":precio_venta}
            precio_total += precio_venta
            cantidad_total += cantidad
            iguales = 0
            for j in productos:
                if producto["codigo"] == j["codigo"]:
                    print("\nEl producto ya esta en la canasta, inserte otro: ")
                    continue
            
            productos.append(producto)
            
                
        except:
            print("\nHubo un error agregando el producto intente nueva mente: ")
        while(True):
            try:
                comando = int(input("\nDigite 1 para continuar agregando productos o 0 para salir: "))
                break
            except:
                print("\nNo he entenido el comando: ")
                
        
        if comando == 0:
            agregar = False
    venta = [productos, vendedor, comprador, time, cantidad_total, precio_total]
    return venta
    




def imprimir(venta):
    i=0
    f = open('recibo.txt', 'w')
    recibo = ('' + '\n'
            +'                 RECIBO DE PAGO                    ' + '\n'
            +'                                                   ' + '\n'
            +'    Nombre del vendedor:   '+venta[1]+'            ' + '\n'
            '                                                    ' + '\n'
            +'    Nombre del comprador:   '+venta[2]+'           ' + '\n'
            +'                                                   ' + '\n'
            +'    Cantidad de productos: '+str(venta[4])+'           ' + '\n')
   
    for productos in venta[0]:
       i = int(i)
       i += 1
       i = str(i)

       precio = str(productos["precio"])
       precio_venta = str(productos["precio_venta"])
       cantidad = str(productos["cantidad"])
       recibo = recibo + ('\n    #:'+i+'   '+productos["nombre"] +'    '+ cantidad+'     ' 
       + '\n     Precio por unidad: '+ precio + '      Precio total: ' + precio_venta +'     \n' )
       
    recibo += ('                                              ' + '\n'
                 +'                                              ' + '\n'
                +'                                               ' + '\n'
                +'        CANTIDAD TOTAL DE PRODUCTOS: '+str(venta[4])+' ' + '\n'
                +'        PRECIO TOTAL: '+str(venta[5])+'        ' + '\n'
                '                                              ' + '\n'
                 +'                                              ' + '\n'
                +'______________________________________________________________' + '\n'
                +'                                              ' + '\n'
                +'                 Gracias por su compra        ' + '\n'
                +'                  '+venta[3]+'              ' + '\n')
    f.write(recibo)

       

imprimir(venta())



        
