from docxtpl import DocxTemplate
from datetime import datetime
import calendar
import tkinter as tk
from tkinter import filedialog
from num2words import num2words

def generar_acta_entrega(administrador,contratista,factura):
    
    docActaEntrega = DocxTemplate("aplicacion\plantillas\ACTA DE ENTREGA RECEPCIÓN PARCIAL.docx")

    def cifra_a_texto(monto):
        
        # Convertir monto a float si es una cadena
        monto = float(monto)
        
        # Obtener parte entera y decimal
        parte_entera, parte_decimal = f"{monto:.2f}".split(".")
        
        # Convertir parte entera a palabras
        parte_entera_texto = num2words(int(parte_entera), lang="es")

        # Formatear resultado
        resultado = f"{parte_entera_texto} con {parte_decimal}/100 dólares de los Estados Unidos de América"
        return resultado
    

    

    def fecha_a_texto(f,fecha):
        fecha_texto="DD-MM-AAAA"
        # Diccionario de meses en español
        meses = {
            "01": "enero", "02": "febrero", "03": "marzo", "04": "abril", "05": "mayo", "06": "junio",
            "07": "julio", "08": "agosto", "09": "septiembre", "10": "octubre", "11": "noviembre", "12": "diciembre"
        }

        # Convertir la fecha en un objeto datetime
        fecha_dt = datetime.strptime(fecha, "%d-%m-%Y")

        # Extraer día, mes y año
        dia = fecha_dt.day
        mes = meses[fecha_dt.strftime("%m")]  # Obtener el nombre del mes
        año = fecha_dt.year
        if f=="f1":
            fecha_texto=f"{dia:02} días del mes de {mes} de {año}"
        elif f=="f2":
            fecha_texto=f"{dia:02} de {mes} del {año}"
        # Retornar la fecha en el formato deseado
        return fecha_texto
    
    def obtener_planilla():
        # Diccionario de meses con su número correspondiente
        meses = {
            "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4, "Mayo": 5, "Junio": 6,
            "Julio": 7, "Agosto": 8, "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
        }

        # Convertir la fecha de inicio a un objeto datetime
        fecha_dt = datetime.strptime(contratista[4], "%d-%m-%Y")
        
        # Obtener el mes de inicio del contrato
        mes_inicio = fecha_dt.month

        # Obtener el número del mes de pago
        mes_pago_num = meses.get(factura[4])

        
        numero_planilla = (mes_pago_num - mes_inicio + 12) % 12 + 1

        return f"{numero_planilla:02}"
        

    contenido = {
        'monto_contrato_a_texto':cifra_a_texto(contratista[3]),
        'costo_mensual_a_texto':cifra_a_texto(contratista[9]),
        'nro_planilla':obtener_planilla(),
        'administrador':administrador,
        'fecha_hoy': fecha_a_texto("f1",datetime.today().strftime('%d-%m-%Y')),
        'provincia':contratista[11],
        'localidades':contratista[10],
        'nro_factura':factura[2],
        'orden': contratista[1],
        'fecha': factura[3],
        'empresa': contratista[2],
        'mes_pago': factura[4],
        'anio_pago':factura[5],
        'monto_contrato': contratista[3],
        'costo_mensual': contratista[9],
        'fecha_inicio': fecha_a_texto("f2",contratista[4]),
        'ruc': contratista[8],
        'ficha':contratista[12]
    }
    docActaEntrega.render(contenido)
    nombre_archivo = str("Acta Entrega Recepcion")
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter
    root.attributes('-topmost', True)  # Asegurar que esté al frente
    root.update()  # Refrescar la ventana antes de abrir el diálogo

    
    ruta_guardado = filedialog.asksaveasfilename(
        defaultextension=".docx",
        filetypes=[("Documentos Word", "*.docx")],
        initialfile=nombre_archivo,
        title="Guardar acta de entrega"
    )

    # Guardar el documento si se seleccionó una ruta
    if ruta_guardado:
        doc.save(ruta_guardado)
        print(f"Archivo guardado en: {ruta_guardado}")
    else:
        print("Guardado cancelado.")

   




