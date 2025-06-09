from controlador.controlador_principal import Controlador_Principal
import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.Colors.WHITE
    page.title="Gestor de Contratos"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.theme = ft.Theme(color_scheme=ft.ColorScheme(primary=ft.Colors.BLACK))
  

    controlador = Controlador_Principal(page)
    controlador.mostrar_vista()

 

ft.app(target=main) 