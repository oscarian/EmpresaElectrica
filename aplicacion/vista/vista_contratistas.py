import flet as ft
from controlador import controlador_contratista


datos_contratista={}
def obtener_pantalla_contratistas(): #debo hacer validaciones
            
        orden = ft.TextField(dense=True,label="Orden", border_color= ft.Colors.GREY_100,bgcolor=ft.Colors.GREY_50)
        empresa = ft.TextField(dense=True,label="Empresa",border_color= ft.Colors.GREY_100,bgcolor=ft.colors.GREY_50)
        monto_contrato = ft.TextField(dense=True,label="Monto Contrato",border_color= ft.Colors.GREY_100,bgcolor=ft.colors.GREY_50)
        fecha_inicio = ft.TextField(dense=True,label="Fecha Inicio",border_color= ft.Colors.GREY_100,bgcolor=ft.colors.GREY_50)
        fecha_finalizacion = ft.TextField(dense=True,label="Fecha Finalización",border_color= ft.Colors.GREY_100,bgcolor=ft.colors.GREY_50)
        fecha_emision = ft.TextField(dense=True,label="Fecha Emisión",border_color= ft.Colors.GREY_100,bgcolor=ft.colors.GREY_50)
        fecha_suscripcion = ft.TextField(dense=True,label="Fecha Suscripción",border_color= ft.Colors.GREY_100,bgcolor=ft.colors.GREY_50)
        ruc = ft.TextField(dense=True,label="RUC",border_color= ft.Colors.GREY_100,bgcolor=ft.colors.GREY_50)
        costo_mensual = ft.TextField(dense=True,label="Costo Mensual",border_color= ft.Colors.GREY_100,bgcolor=ft.colors.GREY_50)
        localidad = ft.TextField(dense=True,label="Localidad",border_color= ft.Colors.GREY_100,bgcolor=ft.colors.GREY_50)
        provincia = ft.TextField(dense=True,label="Provincia",border_color= ft.Colors.GREY_100,bgcolor=ft.colors.GREY_50)
        ficha= ft.TextField(dense=True,label="Ficha Específica",border_color= ft.Colors.GREY_100,bgcolor=ft.colors.GREY_50)
        
        
            
        def limpiar():
             ficha.value=orden.value = empresa.value = monto_contrato.value = fecha_inicio.value = fecha_finalizacion.value = fecha_emision.value = fecha_suscripcion.value = ruc.value = costo_mensual.value= provincia.value = localidad.value = ""
                
             
        
        def validar_formulario_contratista():
             print("Hay que validar los datos del formulario")
             return True
        
        #me quede aqui no se esta guardando el campo ficha

        def agregar_contratista(e): #debo hacer validaciones
            if validar_formulario_contratista()==True:
                datos_contratista = {
                    'orden': orden.value,
                    'empresa': empresa.value,
                    'monto_contrato': monto_contrato.value,
                    'fecha_inicio': fecha_inicio.value,
                    'fecha_finalizacion': fecha_finalizacion.value,
                    'fecha_emision': fecha_emision.value,
                    'fecha_suscripcion': fecha_suscripcion.value,
                    'ruc': ruc.value,
                    'costo_mensual': costo_mensual.value,
                    'localidad': localidad.value,
                    'provincia': provincia.value,
                    'ficha':ficha.value
                }

                controlador_contratista.agregar_contratista(datos_contratista)
                limpiar()
                show_data()
                
                e.page.update()
                print("Se ha agregado corretamente el contratista")
        
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
                                #ft.DataColumn(ft.Text("Id Contratista", color=ft.colors.BLUE_800, weight = "bold")),
                                #ft.DataColumn(ft.Text("Orden", color=ft.colors.BLUE_800, weight = "bold")),
                                ft.DataColumn(ft.Text("Empresa", color=ft.colors.BLUE_800, weight = "bold")),
                                ft.DataColumn(ft.Text("Monto Total", color=ft.colors.BLUE_800, weight = "bold"), numeric=True),
                                ft.DataColumn(ft.Text("Costo Mensual", color=ft.colors.BLUE_800, weight = "bold"), numeric=True ),
                            ],
                        )        
        
       
        

        def show_data():
            tabla_datos.rows = []
            
            contratos = controlador_contratista.obtener_contratistas()
            
            for contrato in contratos:
                tabla_datos.rows.append(
                    ft.DataRow(
                        ##on_select_changed=get_index, 
                        cells=[
                            #ft.DataCell(ft.Text(f"{contrato[0]}")),
                            #ft.DataCell(ft.Text(f"{contrato[1]}")),  
                            ft.DataCell(ft.Text(f"{contrato[2]}")),  
                            ft.DataCell(ft.Text(f"{contrato[3]}")),
                            ft.DataCell(ft.Text(f"{contrato[9]}")),  
                        ]
                    )
                )
            
        
        show_data()
        
        formulario = ft.Container(
            bgcolor=ft.colors.WHITE,
            border_radius=0,
            col=4,
            padding=ft.padding.all(10),
            content=ft.Column(
                #alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    # Contenedor para organizar en dos columnas
                    ft.Row(
                        alignment=ft.MainAxisAlignment.START,
                        controls=[
                            # Primera columna
                            ft.Column(
                                expand= True, 
                                scroll="auto",
                                controls=[
                                    orden,
                                    empresa,
                                    ruc,
                                    ficha,
                                    monto_contrato,
                                    costo_mensual,
                                ]
                            ),
                            # Segunda columna
                            ft.Column(
                                expand= True, 
                                scroll="auto",
                                controls=[
                                    fecha_inicio,
                                    fecha_finalizacion,
                                    fecha_emision,
                                    fecha_suscripcion,
                                    localidad,
                                    provincia,
                                    
                                ]
                            ),
                        ]
                    ),
                    
                    
                    # Botones alineados al centro
                    ft.Container(
                        content=ft.Row(
                            spacing=5,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.TextButton(
                                    text="Guardar",
                                    icon=ft.icons.SAVE,
                                    icon_color="white",
                                    style=ft.ButtonStyle(color="white", bgcolor=ft.colors.BLUE_800),
                                    on_click=agregar_contratista,
                                ),
                                ft.TextButton(
                                    text="Actualizar",
                                    icon=ft.icons.UPDATE,
                                    icon_color="white",
                                    style=ft.ButtonStyle(color="white", bgcolor=ft.colors.BLUE_800),
                                    # on_click=update_data,
                                ),
                                ft.TextButton(
                                    text="Borrar",
                                    icon=ft.icons.DELETE,
                                    icon_color="white",
                                    style=ft.ButtonStyle(color="white", bgcolor=ft.colors.BLUE_800),
                                    # on_click=delete_data,
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