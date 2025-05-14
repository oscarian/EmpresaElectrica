import flet as ft
from vista import vista_contratistas
from vista import vista_facturas
from vista import vista_informes

<<<<<<< Updated upstream
=======
#hasta aqui
>>>>>>> Stashed changes

class Vista_Principal:
    def __init__(self, page):
        self.page = page 
    
    def crear_pantalla_principal(self):

        
        def cambiar_contenido(e):
            if tabs.selected_index==1:
                tab2.content=vista_facturas.obtener_pantalla_facturas()
            if tabs.selected_index==2:
                tab3.content=vista_informes.obtener_pantalla_informes()
            tabs.update()

        # Definir tabs con contenido inicial
        tab1 = ft.Tab(text="Contratistas",icon=ft.icons.PERSON,content=vista_contratistas.obtener_pantalla_contratistas())
        tab2 = ft.Tab(text="Facturas",icon=ft.icons.PERSON,content=vista_facturas.obtener_pantalla_facturas())
        tab3 = ft.Tab(text="Informes",icon=ft.icons.PERSON,content=vista_informes.obtener_pantalla_informes())

        # Tabs principal
        tabs = ft.Tabs(
            on_change=cambiar_contenido,
            animation_duration=0,
            selected_index=0,
            expand=1,
            label_color=ft.colors.BLACK,
            unselected_label_color=ft.colors.BLUE_200,
            tabs=[tab1, tab2,tab3]
        )

        # Botón para cambiar el contenido de la pestaña 2
        titulo=ft.Text(value="Gestión de Contratistas",size=24,color=ft.colors.BLUE_800)
        
        self.page.add(titulo,tabs)

