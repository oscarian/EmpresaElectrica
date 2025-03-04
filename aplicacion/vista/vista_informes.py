import flet as ft
from controlador import controlador_contratista
from controlador import controlador_factura
from controlador import controlador_informes
from controlador.controlador_documentos import Generar_Docs

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
                      
                      contDocs.generar() 
                      #controlador_informes.generar_acta_entrega(administrador.value,contratista,factura)
                      

            """if c1.value==True:
                contratistas = controlador_contratista.obtener_contratistas()
                facturas = controlador_factura.obtener_facturas()
                for contratista in contratistas:
                    if c.value==contratista[2]:
                        for factura in facturas:
                            if f.value==factura[4]:
                                controlador_informes.generar_acta_entrega(administrador.value,contratista,factura)
                
                e.page.update()"""

        t = ft.Text()
        c1 = ft.Checkbox(label="Acta de Entrega/Recepción", value=False)
        c2 = ft.Checkbox(label="Informe Administrador", value=False)
        word = ft.Checkbox(label="Crear Word", value=False)
        pdf = ft.Checkbox(label="Crear PDF", value=False)
       
        generar_button = ft.ElevatedButton(text="Generar", on_click=generar_informes)
        
        
        formulario = ft.Container(
            bgcolor= ft.Colors.WHITE10,
            border_radius=10,
            col = 8,
            padding=ft.padding.all(10),
            content= ft.Column(   
                expand=True,           
                controls=[
                    administrador,
                    dropdown_contratista,
                    dropdown_factura,
                    c1, c2, word, pdf, generar_button, t,
                ]
            )
        )
        
        conent = ft.ResponsiveRow(
            controls=[
                formulario,
            ]
        )

        return ft.Container(conent) 