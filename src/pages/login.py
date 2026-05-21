import flet as ft
from requests import Response

from api.clientstorage import ClientStorage
from api.auth.login import auth_login
from appstate import AppState
from style.style import Colors

class LoginPage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "/login"

        self.state = AppState()

        self.padding = 0
        self.spacing = 0

        self.bgcolor = Colors.BLACK_BACKGROUND

        self.vertical_alignment = ft.MainAxisAlignment.START
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.expand = True

        self.prefs = ft.SharedPreferences()
        self.storage = ClientStorage(self.prefs)


        self.login = ft.TextField(
                        hint_text="Nome de Usuário",
                        mouse_cursor=ft.MouseCursor.TEXT,
                        border_radius=30,
                        border=ft.InputBorder.OUTLINE,
                        border_color=ft.Colors.TRANSPARENT,
                        text_style=ft.TextStyle(
                            color=ft.Colors.BLACK
                        ),
                        hint_style=ft.TextStyle(
                            color=ft.Colors.BLACK_45
                        ),
                        label_style=ft.TextStyle(
                            color=ft.Colors.BLACK_45
                        ),
                        bgcolor=ft.Colors.WHITE,
                        # on_change=self.handle_user
                    )

        self.password = ft.TextField(
                            hint_text="**********",
                            password=True,
                            can_reveal_password=True,
                            mouse_cursor=ft.MouseCursor.TEXT,
                            border_radius=30,
                            border=ft.InputBorder.OUTLINE,
                            border_color=ft.Colors.TRANSPARENT,
                            text_style=ft.TextStyle(
                                color=ft.Colors.BLACK
                            ),
                            hint_style=ft.TextStyle(
                                color=ft.Colors.BLACK_45
                            ),
                            label_style=ft.TextStyle(
                                color=ft.Colors.BLACK_45
                            ),
                            bgcolor=ft.Colors.WHITE,
                        )
        
        self.login_button = ft.Button(
                                content=ft.Text(
                                    value="Entrar",
                                    color=ft.Colors.WHITE
                                ),
                                width=180,
                                height=45,
                                bgcolor=ft.Colors.GREEN,
                                elevation=5,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(
                                        radius=30
                                    ),
                                    shadow_color=ft.Colors.GREY_700,
                                ),
                                on_click=self.handle_login
                            )

        self.controls = [
            ft.SafeArea(
                expand = True,
                content=ft.Column(
                    controls=[
                        ft.Container(
                            margin=ft.Margin(top=20),
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        src="images/logo_preta.png",
                                        width=80,
                                        height=80
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                expand=True
                            ),
                            # expand=True,
                            alignment=ft.Alignment.CENTER
                        ),
                        ft.Container(
                            margin=ft.Margin(top=30),
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.Text(
                                                value="Bem-vindo!",
                                                text_align=ft.TextAlign(value="center"),
                                                size=24,
                                                weight=ft.FontWeight.W_300
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Text(
                                                value="Informe suas credenciais",
                                                text_align=ft.TextAlign(value="center")
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    ft.Row(
                                        controls=[
                                            self.login
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    ft.Row(
                                        controls=[
                                            self.password
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    ft.Row(
                                        controls=[
                                            self.login_button
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Text("Ainda não tem uma conta?"),
                                            ft.TextButton(
                                                content=ft.Text("Cadastre-se")
                                            ),
                                        ],
                                        spacing=2,
                                        alignment=ft.MainAxisAlignment.CENTER
                                    )
                                ],
                                expand=True,
                                alignment=ft.Alignment.CENTER,
                                spacing=20,
                                margin=ft.Margin(top=30),
                            ),
                            expand=True,
                            alignment=ft.Alignment.CENTER,
                            bgcolor="#1C1C1C",
                            height=page.window.height,
                            border_radius=ft.BorderRadius.only(
                                top_left=30,
                                top_right=30
                            ),
                            shadow=ft.BoxShadow(
                                spread_radius=0,
                                blur_radius=1,
                                color=ft.Colors.GREEN_300,
                                offset=ft.Offset(0, -2),
                                blur_style=ft.BlurStyle.NORMAL
                            )
                        ),                       
                    ]
                ),
            )
        ]

    async def handle_login(self, e):

        snackbar = ft.SnackBar(
            content=ft.Text("Aviso"),
            duration=2000,
            show_close_icon=True,
        )

        if not self.login.value:
            snackbar.content = ft.Text(
                value="O campo de usuário é obrigatório!",
                color=ft.Colors.BLACK,
            )
            snackbar.bgcolor = ft.Colors.YELLOW_400
            self.page.show_dialog(snackbar)
            self.page.update()
            return

        if not self.password.value:
            snackbar.content = ft.Text(
                value="O campo de senha é obrigatório!",
                color=ft.Colors.BLACK,
            )
            snackbar.bgcolor = ft.Colors.YELLOW_400
            self.page.show_dialog(snackbar)
            self.page.update()
            return

        r: Response = await auth_login(self.page, self.login.value, self.password.value)
        req = r.json()

        if r.status_code == 200:
            snackbar.content = ft.Text("Usuário logado com sucesso!")
            snackbar.bgcolor = Colors.VERDE_BOTI
            self.page.show_dialog(snackbar)
            self.page.update()

            await self.storage.set_token(req["access_token"], req["refresh_token"])

            if not await self.storage.is_authenticated():
                snackbar.content = ft.Text(
                    value="Ocorreu um erro ao salvar suas credenciais!",
                    color=ft.Colors.WHITE
                )
                snackbar.bgcolor = ft.Colors.YELLOW_400
                self.page.show_dialog(snackbar)
                self.page.update()
                return

            await self.page.push_route("/")
        else:
            snackbar.content = ft.Text(
                value=f"Erro: {req['detail']}!",
                color=ft.Colors.WHITE
            )
            snackbar.bgcolor = Colors.VERMELHO_OUI
            self.page.show_dialog(snackbar)
            self.page.update()

