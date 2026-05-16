from typing import List

import flet as ft

from components.header import Header
from style.style import Colors

class ReceiveInitialPage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.spacing = 0
        self.padding = 0

        self.scroll = ft.ScrollMode.ADAPTIVE

        self.bgcolor = Colors.BLACK_BACKGROUND

        self.vertical_alignment = ft.MainAxisAlignment.START
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.expand = True

        self.route = "/receive/initial"

        tipos_mov = [
            "REGULAR",
            "BAIXA",
            "VENDA"
        ]

        lojas = [
            "LOJA 1",
            "LOJA 2",
            "LOJA 3"
        ]

        def set_items_menu(data: List[str], texto_value: ft.Text) -> List[ft.PopupMenuItem]:
            items_menu = [
                ft.PopupMenuItem(
                    content=mov,
                    data=mov,
                    on_click=lambda e: set_value(e, texto_value),
                    expand=True, 
                ) for mov in data
            ]

            page.update()

            return items_menu

        texto_movimentacao = ft.Text(
            value="REGULAR", 
            size=20, 
            color=ft.Colors.WHITE
        )

        texto_loja = ft.Text(
            value="Loja 4178",
            size=20,
            color=ft.Colors.WHITE
        )

        texto_usuario = ft.Text(
            value="Usuário",
            size=20,
            color=ft.Colors.WHITE
        )

        def set_value(e, texto_value):
            print(e.control.data)
            texto_value.value = e.control.data
            page.update()


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
                                                    texto_movimentacao
                                                ],
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                expand=True,
                                                margin=ft.Margin(
                                                    left=20
                                                ),
                                            ),
                                            ft.PopupMenuButton(
                                                icon=ft.Icon(
                                                    icon=ft.Icons.KEYBOARD_ARROW_DOWN_ROUNDED,
                                                    color=ft.Colors.GREY,
                                                    size=40
                                                ),
                                                items=set_items_menu(tipos_mov, texto_movimentacao),
                                                menu_position=ft.PopupMenuPosition.OVER,
                                                disabled=True
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
                                                        "LOJA DE ORIGEM"
                                                    ),
                                                    texto_loja
                                                ],
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                expand=True,
                                                margin=ft.Margin(
                                                    left=20
                                                ),
                                            ),
                                            ft.PopupMenuButton(
                                                icon=ft.Icon(
                                                    icon=ft.Icons.STORE_OUTLINED,
                                                    color=ft.Colors.GREY,
                                                    size=40
                                                ),
                                                items=set_items_menu(lojas, texto_loja),
                                                menu_position=ft.PopupMenuPosition.OVER,
                                                disabled=True
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
                                                        "RESPONSÁVEL PELO RECEBIMENTO"
                                                    ),
                                                    texto_usuario
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
                                                        width=page.width * 0.8,
                                                        disabled=True
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
                            on_click=lambda _ : page.run_task(page.push_route, "/receive/insert")
                        )
                    ],
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                bgcolor=ft.Colors.TRANSPARENT,
            )