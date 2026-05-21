from typing import List

import flet as ft

from api.clientstorage import ClientStorage
from api.routes.branch_route import list_branchs
from api.schemas.branch import Branch
from components.header import Header
from style.style import Colors

class SendInitialPage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.spacing = 0
        self.padding = 0

        self.scroll = ft.ScrollMode.ADAPTIVE

        self.bgcolor = Colors.BLACK_BACKGROUND

        self.vertical_alignment = ft.MainAxisAlignment.START
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.expand = True

        self.route = "/send/initial"

        self.prefs = ft.SharedPreferences()
        self.storage = ClientStorage(self.prefs)

        self.tipos_mov = [
            "REGULAR",
            "BAIXA",
            "VENDA"
        ]

        self.select_tipo_movimentacao = ft.PopupMenuButton(
                                            items=[
                                                ft.PopupMenuItem(
                                                    content=ft.Text(
                                                        value="REGULAR"
                                                    )
                                                )
                                            ],
                                            icon=ft.Icon(
                                                icon=ft.Icons.KEYBOARD_ARROW_DOWN_ROUNDED,
                                                color=Colors.VERDE_BOTI,
                                                size=40
                                            ),
                                            menu_position=ft.PopupMenuPosition.OVER,
                                        )

        self.select_loja_destino: ft.PopupMenuButton = ft.PopupMenuButton(
                                        icon=ft.Icon(
                                            icon=ft.Icons.STORE_OUTLINED,
                                            color=Colors.VERDE_BOTI,
                                            size=40
                                        ),
                                        menu_position=ft.PopupMenuPosition.OVER,
                                    )

        self.texto_movimentacao = ft.Text(
            value="REGULAR", 
            size=20, 
            color=ft.Colors.WHITE
        )

        self.texto_loja = ft.Text(
            value="Selecionar unidade",
            size=20,
            color=ft.Colors.WHITE
        )

        self.texto_usuario = ft.Text(
            value="Usuário",
            size=20,
            color=ft.Colors.WHITE
        )

        
        self.controls = [
            ft.SafeArea(
                content=ft.Column(
                    controls=[
                        ft.Container(
                            content=Header(
                                "Configuração Inicial", 
                                [1, 3], 
                                page, 
                                "/"
                            ),
                            padding=ft.Padding(
                                top=10,
                                bottom=10
                            ),
                            gradient=ft.LinearGradient(
                                begin=ft.Alignment.BOTTOM_CENTER,
                                end=ft.Alignment.TOP_CENTER,
                                colors=[
                                    "#121212",
                                    "#212121",
                                    # "#717171"
                                ],
                                stops=[
                                    0.5,
                                    1
                                ]
                            ),
                            border_radius=ft.BorderRadius.only(
                                bottom_left=30,
                                bottom_right=30
                            ),
                            shadow=ft.BoxShadow(
                                spread_radius=-10,
                                blur_radius=15,
                                color="#808080"
                            )
                        ),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Row(
                                        controls=[
                                            ft.Column(
                                                controls=[
                                                    ft.Text(
                                                        "TIPO MOVIMENTAÇÃO"
                                                    ),
                                                    self.texto_movimentacao
                                                ],
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                expand=True,
                                                margin=ft.Margin(
                                                    left=20
                                                ),
                                            ),
                                            self.select_tipo_movimentacao
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    ),
                                    bgcolor=Colors.CINZA_CONTAINER,
                                    shadow=ft.BoxShadow(
                                        blur_radius=1,
                                        color=ft.Colors.GREY,
                                        offset=ft.Offset(1, 3)
                                    ),
                                    margin=ft.Margin(
                                        top=20
                                    ),
                                    height=80,
                                    width=page.width * 0.9,
                                    border_radius=20
                                ),
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Row(
                                        controls=[
                                            ft.Column(
                                                controls=[
                                                    ft.Text(
                                                        "LOJA DE DESTINO"
                                                    ),
                                                    self.texto_loja
                                                ],
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                expand=True,
                                                margin=ft.Margin(
                                                    left=20
                                                ),
                                            ),
                                            self.select_loja_destino
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    ),
                                    bgcolor=Colors.CINZA_CONTAINER,
                                    shadow=ft.BoxShadow(
                                        blur_radius=1,
                                        color=ft.Colors.GREY,
                                        offset=ft.Offset(1, 3)
                                    ),
                                    margin=ft.Margin(
                                        top=20
                                    ),
                                    height=80,
                                    width=page.width * 0.9,
                                    border_radius=20
                                ),
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Row(
                                        controls=[
                                            ft.Column(
                                                controls=[
                                                    ft.Text(
                                                        "RESPONSÁVEL PELO ENVIO"
                                                    ),
                                                    self.texto_usuario
                                                ],
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                expand=True,
                                                margin=ft.Margin(
                                                    left=20
                                                ),
                                            ),
                                            ft.IconButton(
                                                icon=ft.Icon(
                                                    icon=ft.Icons.LOCK_PERSON_OUTLINED,
                                                    size=40,
                                                    color=ft.Colors.GREY
                                                ),
                                                disabled=True,
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    ),
                                    bgcolor=Colors.CINZA_CONTAINER,
                                    shadow=ft.BoxShadow(
                                        blur_radius=1,
                                        color=ft.Colors.GREY,
                                        offset=ft.Offset(1, 3)
                                    ),
                                    margin=ft.Margin(
                                        top=20
                                    ),
                                    height=80,
                                    width=page.width * 0.9,
                                    border_radius=20
                                ),
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Row(
                                        controls=[
                                            ft.Column(
                                                controls=[
                                                    ft.Text(
                                                        "OBSERVAÇÕES"
                                                    ),
                                                    ft.TextField(
                                                        hint_text="Adicione detalhes importantes sobre esta movimentação",
                                                        multiline=True,
                                                        min_lines=1,
                                                        max_lines=3,
                                                        height=page.height * 0.1,
                                                        border=ft.InputBorder.NONE,
                                                        width=page.width * 0.8
                                                    )
                                                ],
                                                alignment=ft.MainAxisAlignment.START,
                                                margin=ft.Margin(
                                                    left=20,
                                                    top=20
                                                ),
                                            )
                                        ]
                                    ),
                                    bgcolor=Colors.CINZA_CONTAINER,
                                    shadow=ft.BoxShadow(
                                        blur_radius=1,
                                        color=ft.Colors.GREY,
                                        offset=ft.Offset(1, 3)
                                    ),
                                    margin=ft.Margin(
                                        top=20
                                    ),
                                    height=page.height * 0.2,
                                    width=page.width * 0.9,
                                    border_radius=20,
                                    alignment=ft.Alignment.CENTER
                                ),
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Container(
                            height=40
                        )
                    ],
                ),
                expand=True
            )
        ]

        self.bottom_appbar = ft.BottomAppBar(
                content=ft.Row(
                    controls=[
                        ft.Button(
                            content=ft.Row(
                                controls=[
                                    ft.Text(
                                        value="CONTINUAR",
                                        style=ft.TextStyle(
                                            color=ft.Colors.WHITE,
                                            size=18
                                        )
                                    ),
                                    ft.Icon(
                                        icon=ft.Icons.ARROW_RIGHT_ROUNDED,
                                        size=26,
                                        color=ft.Colors.WHITE
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=5
                            ),
                            bgcolor=Colors.VERDE_BOTI,
                            elevation=2,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(
                                    radius=30
                                ),
                                shadow_color=ft.Colors.GREY_700
                            ),
                            width=page.width * 0.9,
                            height=40,
                            on_click=lambda _ : page.run_task(page.push_route, "/send/insert")
                        )
                    ],
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                bgcolor=ft.Colors.TRANSPARENT,
            )

        page.run_task(self.load_data)

    
    async def load_data(self) -> None:
        snackbar = ft.SnackBar(
            content=ft.Text(
                value="OI",
                color=ft.Colors.WHITE
            ),
            bgcolor=Colors.VERMELHO_OUI,
            show_close_icon=True
        )

        is_authenticated = await self.storage.is_authenticated()

        if not is_authenticated:
            self.storage.clear_token()
            self.page.run_task(self.page.push_route("/login"))
            return

        await self.set_menu_tipos_movimentacao()
        await self.set_menu_lojas()
        
    async def set_menu_tipos_movimentacao(self) -> None:
        items = [
            ft.PopupMenuItem(
                content=mov,
                data=mov,
                expand=True, 
            ) for mov in self.tipos_mov
        ]

        self.select_tipo_movimentacao.items = items
        self.select_tipo_movimentacao.update()
        
    async def set_menu_lojas(self) -> None:

        token = await self.storage.get_access_token()
        branchs: List[Branch] = await list_branchs(token)

        if not branchs:
            await self.storage.clear_token()
            await self.page.push_route("/logout")

        items = [
            ft.PopupMenuItem(
                content=ft.Text(
                    value=f"{loja.pdv} - {loja.name}"
                ),
                data=loja.pdv,
                expand=True
            ) for loja in branchs
        ]

        self.select_loja_destino.items = items
        self.select_loja_destino.update()

    # async def set_value(self, e):
    #         print(e.control.data)
    #         self.page.update()