import flet as ft
from controlador import controlador_contratista
from controlador import controlador_factura

datos_contratista={}
def obtener_pantalla_facturas(): #debo hacer validaciones
        
        nro_factura = ft.TextField(dense=True,label="Número de Factura",border_color= ft.Colors.GREY_100,bgcolor=ft.colors.GREY_50)
        fecha = ft.TextField(dense=True,label="Fecha",border_color= ft.Colors.GREY_100,bgcolor=ft.colors.GREY_50)
        mes_pago=ft.TextField(dense=True,label="Mes de Pago",border_color= ft.Colors.GREY_100,bgcolor=ft.colors.GREY_50)
        anio_pago=ft.TextField(dense=True,label="Año de Pago",border_color= ft.Colors.GREY_100,bgcolor=ft.colors.GREY_50)
        nro_dias = ft.TextField(dense=True,label="Número de días",border_color= ft.Colors.GREY_100,bgcolor=ft.colors.GREY_50)
        valor_factura = ft.TextField(dense=True,label="Valor de la factura",border_color= ft.Colors.GREY_100,bgcolor=ft.colors.GREY_50)
        dias_multa=ft.TextField(dense=True,label="Días de Multa",border_color= ft.Colors.GREY_100,bgcolor=ft.colors.GREY_50)
        
        contratos = controlador_contratista.obtener_contratistas()
        def dropdown_changed(e):
            t.value = f"{dropdown_factura.value}"
        t=ft.Text() 

        dropdown_factura =ft.Dropdown(on_change=dropdown_changed, label="Contratista", hint_text="Escoja un contratista", autofocus=True)
        dropdown_factura.options.clear
        for contrato in contratos:
                dropdown_factura.options.append(ft.dropdown.Option(contrato[2]))
        
        
        def limpiar():
             dias_multa.value=  nro_factura.value = fecha.value = mes_pago.value=dias_multa.value= anio_pago.value = nro_dias.value  = ""
                
             
        
        def validar_formulario_factura():
             print("Hay que validar los datos del formulario")
             return True
        
        

        
        
    #Botones formulario Contratista
        
        ###boton_guardar=ft.ElevatedButton("Guardar Contratista",on_click=agregar_factura)
        
        campo_busqueda = ft.TextField(                        
                            suffix_icon = ft.icons.SEARCH,
                            label= "Buscar por el nombre",
                            border= ft.InputBorder.UNDERLINE,
                            border_color= ft.colors.BLUE_800,
                            label_style = ft.TextStyle(color= ft.colors.BLUE_800),
                            ###on_change = searh_data,
                        )     
      
        tabla_datos =  ft.DataTable(
                            expand= True,
                            border=ft.border.all(2, "ft.colors.BLUE_800"),
                            #data_row_color = { ft.MaterialState.SELECTED: ft.colors.BLUE_800, ft.MaterialState.PRESSED: "black"},
                            border_radius=10,
                            show_checkbox_column = True,
                            columns=[
                                ft.DataColumn(ft.Text("Contratista", color=ft.colors.BLUE_800, weight = "bold")),
                                ft.DataColumn(ft.Text("Nro Factura", color=ft.colors.BLUE_800, weight = "bold")),
                                ft.DataColumn(ft.Text("Fecha", color=ft.colors.BLUE_800, weight = "bold")),
                                ft.DataColumn(ft.Text("Mes de Pago", color=ft.colors.BLUE_800, weight = "bold")),
                                ft.DataColumn(ft.Text("Año de Pago", color=ft.colors.BLUE_800, weight = "bold"), numeric=True),
                                ft.DataColumn(ft.Text("Valor", color=ft.colors.BLUE_800, weight = "bold"), numeric=True ),
                            ],
                        )        
        
       
        

        def show_data():
            tabla_datos.rows = []
            
            contratos = controlador_contratista.obtener_contratistas()
            facturas = controlador_factura.obtener_facturas()
            nombre_contratista=ft.Text()
            for factura in facturas:
                for contrato in contratos:
                    if factura[1]==contrato[0]:
                        nombre_contratista=contrato[2]
                        break
                tabla_datos.rows.append(
                    ft.DataRow(
                        ##on_select_changed=get_index, 
                        cells=[
                            ft.DataCell(ft.Text(nombre_contratista)),
                            ft.DataCell(ft.Text(f"{factura[2]}")),  
                            ft.DataCell(ft.Text(f"{factura[3]}")),
                            ft.DataCell(ft.Text(f"{factura[4]}")),
                            ft.DataCell(ft.Text(f"{factura[5]}")),
                            ft.DataCell(ft.Text(f"{factura[5]}"))  
                        ]
                    )
                )
            
        
        show_data()


        def agregar_factura(e): #debo hacer validaciones
            if validar_formulario_factura()==True:
                id_contratista=ft.Text()
                for contrato in contratos:
                    if t.value==contrato[2]:
                        id_contratista=contrato[0]
                        break
                datos_contratista = {
                    'id_contratista':id_contratista,
                    'nro_factura': nro_factura.value,
                    'fecha': fecha.value,
                    'mes_pago':mes_pago.value,
                    'anio_pago':anio_pago.value,
                    'nro_dias':nro_dias.value,
                    'valor_factura':valor_factura.value,
                    'dias_multa':dias_multa.value,
                }
                controlador_factura.agregar_factura(datos_contratista)
                limpiar()
                show_data()
                e.page.update()
                
                print("Se ha agregado corretamente el contratista")
        

        formulario = ft.Container(
            bgcolor=ft.colors.WHITE,
            border_radius=0,
            col=4,
            padding=ft.padding.all(10),
            content= ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                controls=[
                    dropdown_factura,    
                    nro_factura,
                    fecha,
                    mes_pago,
                    anio_pago,
                    nro_dias,
                    valor_factura,
                    dias_multa,
                    
                    
                    ft.Container(
                        content= ft.Row(
                            spacing = 5,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls= [
                            ft.TextButton(text="Guardar",
                                        icon = ft.icons.SAVE,
                                        icon_color= "white",
                                        style= ft.ButtonStyle(color = "white",  bgcolor =ft.colors.BLUE_800),
                                        
                                        on_click= agregar_factura,
                                        ),
                            ft.TextButton(text="Actualizar",
                                        icon = ft.icons.UPDATE,
                                        icon_color= "white",
                                        style= ft.ButtonStyle(color = "white",  bgcolor =ft.colors.BLUE_800),
                                        ###on_click=update_data,
                                        ),    
                            ft.TextButton(text="Borrar",
                                        icon = ft.icons.DELETE,
                                        icon_color= "white",
                                        style= ft.ButtonStyle(color = "white",  bgcolor =ft.colors.BLUE_800),
                                        ###on_click= delete_data,
                                        ),                          
                            ]
                        )
                        
                    )
                ]
            )
        )

        table = ft.Container(
            bgcolor= ft.Colors.WHITE10,
            border_radius=10,
            col = 8,
            padding=ft.padding.all(10),
            content= ft.Column(   
                expand=True,           
                controls=[
                    ft.Container(
                        padding = 10,
                        content= ft.Row(
                            controls=[
                                campo_busqueda,
                                ft.IconButton(
                                    icon= ft.icons.EDIT,
                                    ###on_click= edit_flied_text,
                                    icon_color= ft.Colors.GREY_800,
                                ),
                                  
                            ]
                        ),
                    ),

                    ft.Column(
                        expand= True, 
                        scroll="auto",
                        controls=[
                        ft.ResponsiveRow([
                            tabla_datos
                            ]),
                        ]
                    )
                ]
            )
        )
        conent = ft.ResponsiveRow(
            controls=[
                formulario,
                table
            ]
        )

        return ft.Container(conent) 