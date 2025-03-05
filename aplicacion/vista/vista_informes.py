import flet as ft
from controlador import controlador_contratista
from controlador import controlador_factura
from controlador.controlador_documentos import Generar_Docs
import tkinter as tk
from tkinter import messagebox

def obtener_pantalla_informes(): #debo hacer validaciones
        

        administrador = ft.TextField(dense=True,label="Ingrese el administraor", border_color= ft.Colors.GREY_100,bgcolor=ft.Colors.GREY_50)
        def dropdown_change_contratista(e):
            c.value = f"{dropdown_contratista.value}"
            
        c=ft.Text() 
        dropdown_contratista =ft.Dropdown(on_change=dropdown_change_contratista, label="Contratista", hint_text="Escoja un contratista", autofocus=True)
        
        contratistas = controlador_contratista.obtener_contratistas()
        for contratista in contratistas:
                dropdown_contratista.options.append(ft.dropdown.Option(contratista[2]))
        
        def dropdown_change_facturas(e):
            f.value = f"{dropdown_factura.value}"
        f=ft.Text() 
        dropdown_factura =ft.Dropdown(on_change=dropdown_change_facturas, label="Factura", hint_text="Escoja el mes de facturación", autofocus=True)
        
        facturas = controlador_factura.obtener_facturas()
        for factura in facturas:
                dropdown_factura.options.append(ft.dropdown.Option(factura[4]))
            
        
        def generar_informes(e):
            if word.value==pdf.value==False:
                 print("Seleeccione word o PDF")
            else:
                 if c1.value==c2.value==False:
                      print("Seleccione almenos un documento para generar")
                 else:
                      listaDocs=[c1.value,c2.value]
                      listaWP=[word.value,pdf.value]
                      contDocs=Generar_Docs(listaDocs,listaWP,administrador.value,contratista,factura)
                      valor=contDocs.generar() 
                      print(valor)
                      root = tk.Tk()
                      root.withdraw()
                      if valor == True:
                            messagebox.showinfo("Éxito", "Documentos generados con éxito")
                      else:
                            messagebox.showerror("Error", "No se generó ningún Documento")

                    
                            
                      
        
        c1 = ft.Checkbox(label="Acta de Entrega/Recepción", value=False)
        c2 = ft.Checkbox(label="Informe Administrador", value=False)
        c3 = ft.Checkbox(label="Informe...", value=False)
        c4 = ft.Checkbox(label="Informe...", value=False)
        word = ft.Checkbox(label="Crear Word", value=False)
        pdf = ft.Checkbox(label="Crear PDF", value=False)
       
        generar_button = ft.ElevatedButton(
            text="Generar",
            icon=ft.icons.ADD_CIRCLE,
            icon_color="white",
            style=ft.ButtonStyle(color="white",bgcolor=ft.colors.BLUE_700,),
            on_click=generar_informes,
            animate_scale=ft.Animation(300, ft.AnimationCurve.BOUNCE_OUT),  # Animación al hacer clic
            on_hover=lambda e: (setattr(e.control, "style", ft.ButtonStyle(color="white",bgcolor=ft.colors.BLUE_900 if e.data == "true" else ft.colors.BLUE_800)),e.control.update()),
        )

        
                                    
                                    
                                    
        
        formulario = ft.Container(
            bgcolor= ft.Colors.WHITE10,
            border_radius=50,
            padding=ft.padding.all(50),
            
            content= ft.Column(   
                expand=True,           
                controls=[
                    administrador,
                    dropdown_contratista,
                    dropdown_factura,
                    ft.Divider(color=ft.Colors.LIGHT_BLUE, thickness=2),
                    ft.Row(controls=[ft.Text("Seleccione los documentos a generar:"),]),
                    ft.Row(
                        controls=[c1, c2, c3, c4],
                    ),
                    ft.Divider(color=ft.Colors.LIGHT_BLUE, thickness=2),
                    ft.Row(controls=[ft.Text("Seleccione el formato:"),]),
                    ft.Row(
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[word, pdf],
                    ),
                    ft.Row(
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[generar_button],
                    ),
                ]
            )
        )
        
        conent = ft.ResponsiveRow(
            controls=[
                formulario,
            ]
        )

        return ft.Container(conent) 