from docxtpl import DocxTemplate
from datetime import datetime
import calendar
import tkinter as tk
from tkinter import filedialog
from num2words import num2words
from docx2pdf import convert
import os


class Generar_Docs:
    def __init__(self,listaDocs,listaWP,administrador,contratista,factura):
        self.acta_entrega=listaDocs[0]
        self.informe_administrador=listaDocs[1]
        self.word=listaWP[0]
        self.pdf=listaWP[1]
        self.administrador=administrador
        self.contratista=contratista
        self.factura=factura


    def cifra_a_texto(self,monto):
        
        # Convertir monto a float si es una cadena
        monto = float(monto)
        
        # Obtener parte entera y decimal
        parte_entera, parte_decimal = f"{monto:.2f}".split(".")
        
        # Convertir parte entera a palabras
        parte_entera_texto = num2words(int(parte_entera), lang="es")

        # Formatear resultado
        resultado = f"{parte_entera_texto} con {parte_decimal}/100 dólares de los Estados Unidos de América"
        return resultado


    def fecha_a_texto(self,f,fecha):
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

    def obtener_planilla(self):
        # Diccionario de meses con su número correspondiente
        meses = {
            "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4, "Mayo": 5, "Junio": 6,
            "Julio": 7, "Agosto": 8, "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
        }

        # Convertir la fecha de inicio a un objeto datetime
        fecha_dt = datetime.strptime(self.contratista[4], "%d-%m-%Y")
        
        # Obtener el mes de inicio del contrato
        mes_inicio = fecha_dt.month

        # Obtener el número del mes de pago
        mes_pago_num = meses.get(self.factura[4])

        
        numero_planilla = (mes_pago_num - mes_inicio + 12) % 12 + 1

        return f"{numero_planilla:02}"
    

    
    def generar_acta_entrega(self):
        docActaEntrega = DocxTemplate("aplicacion\plantillas\ACTA DE ENTREGA RECEPCIÓN PARCIAL.docx")
        contenido = {
            'monto_contrato_a_texto':self.cifra_a_texto(self.contratista[3]),
            'costo_mensual_a_texto':self.cifra_a_texto(self.contratista[9]),
            'nro_planilla':self.obtener_planilla(),
            'administrador':self.administrador,
            'fecha_hoy': self.fecha_a_texto("f1",datetime.today().strftime('%d-%m-%Y')),
            'provincia':self.contratista[11],
            'localidades':self.contratista[10],
            'nro_factura':self.factura[2],
            'orden': self.contratista[1],
            'fecha': self.factura[3],
            'empresa': self.contratista[2],
            'mes_pago': self.factura[4],
            'anio_pago':self.factura[5],
            'monto_contrato': self.contratista[3],
            'costo_mensual': self.contratista[9],
            'fecha_inicio': self.fecha_a_texto("f2",self.contratista[4]),
            'ruc': self.contratista[8],
            'ficha':self.contratista[12]
        }
        docActaEntrega.render(contenido)
        return docActaEntrega
    
    def generar_informe_administrador(self):
        documento = DocxTemplate("aplicacion\plantillas\Informe adminsitrador.docx")
        contenido = {
            'monto_contrato_a_texto':self.cifra_a_texto(self.contratista[3]),
            'costo_mensual_a_texto':self.cifra_a_texto(self.contratista[9]),
            'nro_planilla':self.obtener_planilla(),
            'administrador':self.administrador,
            'fecha_hoy': self.fecha_a_texto("f2",datetime.today().strftime('%d-%m-%Y')),
            'localidades':self.contratista[10],
            'orden': self.contratista[1],
            'empresa': self.contratista[2],
            'mes_pago': self.factura[4],
            'anio_pago':self.factura[5],
            'monto_contrato': self.contratista[3],
            'costo_mensual': self.contratista[9],
            'fecha_inicio': self.fecha_a_texto("f2",self.contratista[4]),
            'ficha':self.contratista[12]
        }
        documento.render(contenido)
        return documento

    def generar(self):
        valor=False
        root = tk.Tk()
        root.withdraw()  # Oculta la ventana principal
        root.attributes('-topmost', True)  # Asegurar que esté al frente
        root.update()  # Refrescar la ventana antes de abrir el diálogo

        carpeta_seleccionada = filedialog.askdirectory(title="Selecciona una carpeta")

        if carpeta_seleccionada:
            if self.acta_entrega==True:
                docActaEntrega=self.generar_acta_entrega()
                ruta_word = os.path.join(carpeta_seleccionada, "Acta_Entrega.docx")

                if self.pdf==self.word==True:
                    docActaEntrega.save(ruta_word)
                    ruta_pdf = os.path.join(carpeta_seleccionada, "Acta_Entrega.pdf")
                    convert(ruta_word, ruta_pdf)
                    print("Word y Pdf generados")
                    
                elif self.pdf==False and self.word==True:
                    docActaEntrega.save(ruta_word)
                    print("Se genero solo el Word")
                elif self.pdf==True and self.word==False:
                    docActaEntrega.save(ruta_word)
                    ruta_pdf = os.path.join(carpeta_seleccionada, "Acta_Entrega.pdf")
                    convert(ruta_word, ruta_pdf)
                    os.remove(ruta_word)
                    print("Solo Pdf generados")
            

            if self.informe_administrador==True:
                docInformeAdministrador=self.generar_informe_administrador()
                ruta_word = os.path.join(carpeta_seleccionada, "Informe_Administrador.docx")

                if self.pdf==self.word==True:
                    docInformeAdministrador.save(ruta_word)
                    ruta_pdf = os.path.join(carpeta_seleccionada, "Informe_Administrador.pdf")
                    convert(ruta_word, ruta_pdf)
                    print("Word y Pdf generados")
                elif self.pdf==False and self.word==True:
                    docInformeAdministrador.save(ruta_word)
                    print("Se genero solo el Word")
                elif self.pdf==True and self.word==False:
                    docInformeAdministrador.save(ruta_word)
                    ruta_pdf = os.path.join(carpeta_seleccionada, "Informe_Administrador.pdf")
                    convert(ruta_word, ruta_pdf)
                    os.remove(ruta_word)
                    print("Solo Pdf generados")
            valor=True
        return valor



                
        

