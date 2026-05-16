import flet as ft

from pages.history import HistoryPage
from pages.send.insert import SendItemsPage
from pages.send.revision import SendRevisionPage
from pages.send.initial import SendInitialPage
from pages.receive.initial import ReceiveInitialPage
from pages.receive.insert import ReceiveItemsPage
from pages.receive.revision import ReceiveRevisionPage
from pages.home import HomePage
from pages.loading_page import LoadingPage
from pages.login import LoginPage
from pages.not_found import NotFoundPage
from pages.test import TestPage
from style.style import Colors

async def main(page: ft.Page):
    page.update()
    print(f"Width: {page.width} | Height: {page.height}")
    page.spacing = 0
    page.padding = 0
    page.title = "Boleto Digital"
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.window.bgcolor = ft.Colors.TRANSPARENT
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = Colors.BLACK_BACKGROUND
    # page.window.title_bar_hidden = True
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    router = {
        "/": HomePage,
        "/test": TestPage,
        "/loading": LoadingPage,
        "/login": LoginPage,
        "/history": HistoryPage,
        "/send/initial": SendInitialPage,
        "/send/insert": SendItemsPage,
        "/send/revision": SendRevisionPage,
        "/receive/initial": ReceiveInitialPage,
        "/receive/insert": ReceiveItemsPage,
        "/receive/revision": ReceiveRevisionPage
    }

    def route_change():
        troute = ft.TemplateRoute(page.route)

        page.views.clear()

        if troute.route in router:
            view_content = router[troute.route](page)
            page.views.append(view_content)
        else:
            page.views.append(NotFoundPage(page))
        
        page.update()


    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    await page.push_route("/login")

    route_change()


if __name__ == "__main__":
    ft.run(
        main,
        assets_dir="assets",
        upload_dir="upload"
    )
