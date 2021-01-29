from datetime import datetime
import os
import sys
import time

print('\033[95m'+'\033[1m'+" BIENVENIDO AL SISTEMA DE FACTURACION "+'\033[0m')

def venta():
   
    vendedor = input("\nDigite el nombre del vendedor: ")
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
            for j in productos:
                if codigo == j["codigo"]:
                    print('\033[93m'+"\nEl producto ya esta en la canasta, inserte otro: "+'\033[0m')
                    continue

            cantidad = int(input("\nDigite la cantidad del producto: "))
            precio = float(input("\nDigite el precio del producto: "))
            precio_venta = float((precio * cantidad))
            producto = {"nombre":nombre_producto, "codigo":codigo, "cantidad":cantidad, "precio":precio, "precio_venta":precio_venta}
            precio_total += precio_venta
            cantidad_total += cantidad
            iguales = 0
            
            
            productos.append(producto)
            
                
        except:
            print('\033[91m'+"\nHubo un error agregando el producto intente nueva mente: "+'\033[0m')

        while(True):
            try:
                comando = int(input("\nDigite 1 para continuar agregando productos o 0 para salir: "))
                break
            except:
                print('\033[93m'+"\nNo he entenido el comando: "+'\033[0m')
                
        
        if comando == 0:
            agregar = False

    venta = [productos, vendedor, comprador, time, cantidad_total, precio_total]
    return venta
    




def imprimir(venta):
    

    
    save_path = 'D:/Universidad/Semestre 7/PSP/PSP0/code/recibos/'
    name_of_file = ("recibo")
    completeName = os.path.join(save_path, name_of_file+".txt")
    print("\n Guardando el recibo...")
    time.sleep(2)
    f = open(completeName, 'w')

    recibo = ('' + '\n'
            +'                 RECIBO DE PAGO                    ' + '\n'
            +'                                                   ' + '\n'
            +'    Nombre del vendedor:   '+venta[1]+'            ' + '\n'
            '                                                    ' + '\n'
            +'    Nombre del comprador:   '+venta[2]+'           ' + '\n'
            +'                                                   ' + '\n'
            +'    Cantidad de productos: '+str(venta[4])+'           ' + '\n')
    i = 0
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

    f.close()

i=0   

while(True):
    while(True):
        try:
            comando = int(input("\nDigite: \n-1 Para iniciar una nueva venta."+
                                "\n-2 Para ver los recibos."+
                                "\n-3 Para salir.\n"
                                +"\n\n-"))
            break

        except:

            print('\033[93m'+"\nNo he entendido el comando intenta nuevamente!\n"+'\033[0m')

    if(comando == 1):
        print("\n Iniciando nueva venta!")
        time.sleep(3)
        imprimir(venta())

    elif(comando == 2):
        print("\nBuscando carpeta...\n")
        time.sleep(1)
        print('\033[92m'+"Carpeta encontrada, abriendo directorio\n"+'\033[0m')
        time.sleep(2)
        path = r'D:\\Universidad\Semestre 7\PSP\PSP0\code\recibos'
        os.startfile(path)
        
    elif(comando == 3):
        print("\nSaliendo del sistema!")
        time.sleep(1)
        break

    else:
        print('\033[93m'+"\nNo he entendido el comando intenta nuevamente!\n"+'\033[0m')





        
