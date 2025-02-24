from modelo import modelo_factura

def agregar_factura(datos_factura):
    modelo_factura.agregar_factura(datos_factura)

def obtener_facturas():
    return modelo_factura.obtener_facturas()