from docxtpl import DocxTemplate
from datetime import datetime
import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog

def generar_acta_entrega(contratista,factura):
    doc = DocxTemplate("aplicacion\plantillas\ACTA DE ENTREGA RECEPCIÓN PARCIAL.docx")

    contenido = {
        'provincia':contratista[11],
        'localidades':contratista[10],
        'nro_factura':factura[2],
        'orden': contratista[1],
        'fecha': factura[3],
        'empresa': contratista[2],
        'mes_pago': factura[4],
        'monto_contrato': contratista[3],
        'costo_mensual': contratista[9],
        'fecha_inicio': contratista[4]
    }
    doc.render(contenido)
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

   




