from database.database import crear_tabla_contratos,crear_tabla_facturas
from controlador.controlador_principal import Controlador_Principal
import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.colors.WHITE
    page.title="Gestor de Contratos"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    
    crear_tabla_contratos()
    crear_tabla_facturas()

    controlador = Controlador_Principal(page)
    controlador.mostrar_vista()



ft.app(target=main)