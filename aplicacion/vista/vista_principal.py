import flet as ft
from vista import vista_contratistas
from vista import vista_facturas
from vista import vista_informes

class Vista_Principal:
    def __init__(self, page):
        self.page = page  # Aquí agregamos la página
           

    
    def crear_pantalla_principal(self):


        def pantalla_contratistas():
                return vista_contratistas.obtener_pantalla_contratistas()

        def pantalla_facturas():
                return vista_facturas.obtener_pantalla_facturas()
        
        def pantalla_informes():
                return vista_informes.obtener_pantalla_informes()
       
        #TABS PARA  CONTRATISTAS - FACTURAS - GENENRAR NFORMES
        tabs=ft.Tabs(
            selected_index=0,
            animation_duration=50,
            tabs=[
                ft.Tab(text="Contratistas",icon=ft.icons.PERSON,content=pantalla_contratistas()),
                ft.Tab(text="Facturas",icon=ft.icons.DOCUMENT_SCANNER,content=pantalla_facturas()),
                ft.Tab(text="Generar Informes",icon=ft.icons.SCHEDULE,content=pantalla_informes()),
            ],
            expand=1,
            label_color=ft.colors.BLUE_800,
            unselected_label_color=ft.colors.BLUE_200
            
        )
        titulo=ft.Text(value="Gestón de Contratistas",size=24,color=ft.colors.BLUE_800)
        
        self.page.add(titulo,tabs)
