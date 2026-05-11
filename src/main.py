import flet as ft

from pages.envio.initial_config import InitialConfigEnvio
from pages.envio.insert_items import InsertItems
from pages.insert_itens import SendPage
from pages.home import HomePage
from pages.loading_page import loading_page
from pages.login import LoginPage


async def main(page: ft.Page):
    page.update()
    print(f"Width: {page.width} | Height: {page.height}")
    page.spacing = 0
    page.padding = 0
    page.title = "Boleto Digital"
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.window.bgcolor = ft.Colors.TRANSPARENT
    page.theme_mode = ft.ThemeMode.DARK
    # page.window.title_bar_hidden = True
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def route_change():
        page.views.clear()
        print(f"Rota Atual: {page.route}")
        page.views.append(
            HomePage(page=page)
        )
        if page.route == "/loading":
            page.views.append(
                ft.View(
                    route="/loading",
                    controls=[
                        loading_page(page)
                    ]
                )
            )
        if page.route == "/send":
            page.views.append(
                SendPage(page=page)
            )
        if page.route == "/login":
            page.views.append(
                LoginPage(page)
            )
        if page.route == "/initial_config_envio":
            page.views.append(
                InitialConfigEnvio(page=page)
            )
        if page.route == "/insert_items_envio":
            page.views.append(
                InsertItems(page=page)
            )

                    
        
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    await page.push_route("/insert_items_envio")

    route_change()


if __name__ == "__main__":
    ft.run(
        main,
        assets_dir="assets"
    )
