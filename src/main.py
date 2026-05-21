import flet as ft

from api.clientstorage import ClientStorage
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

    prefs = ft.SharedPreferences()
    page.update()
    storage = ClientStorage(prefs)

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

    async def page_on_connect():
        print("Página reconectada! Testando SharedPreferences...")
        try:
            await ft.SharedPreferences().contains_key("access_token")
            print("SharedPreferences operando - OK...")
        except Exception as ex:
            print(f"Erro detectado na reconexão: {ex}")
            page.window.init()
            page.update()


    async def route_change(e: ft.RouteChangeEvent = ft.RouteChangeEvent):
        troute = ft.TemplateRoute(page.route)
        print(troute.route)

        page.views.clear()

        is_authenticated = await storage.is_authenticated()
        print("AUTH a", is_authenticated)

        # == DESCOMENTAR PARA ATIVAR A OBRIGATORIEDADE DO LOGIN
        if not is_authenticated and page.route != "/login":
            page.route = "/login"

        elif is_authenticated and page.route == "/login":
            page.route = "/"
            page.views.append(router["/"](page))

        elif troute.route == "/logout":
            await storage.clear_token()
            page.route = "/login"
            page.views.append(router["/login"](page))

        elif troute.route in router:
            view_content = router[troute.route](page)
            page.views.append(view_content)

        else:
            page.views.append(NotFoundPage(page))

        page.update()
        

    async def view_pop():
        if page.views:
            page.views.pop()
            top_view = page.views[-1]
            await page.push_route(top_view.route)
        else:
            print("Não tem view")
            await page.push_route(page.route)

    page.on_route_change = await route_change()
    # page.on_view_pop = await view_pop()
    page.on_connect = await page_on_connect()

    # == DESCOMENTAR QUANDO NÃO PRECISAR USAR A AUTENTICAÇÃO
    # await page.push_route("/")

    await page.push_route(page.route)

    await route_change()

    page.update()


if __name__ == "__main__":
    ft.run(
        main,
        assets_dir="assets",
        upload_dir="upload"
    )
