import os
from pathlib import Path
import re

import flet as ft

from components.header import Header
from style.style import Colors

class SendRevisionPage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.route = "/send/revision"

        self.spacing = 0
        self.padding = 0

        self.bgcolor = Colors.BLACK_BACKGROUND

        self.scroll = ft.ScrollMode.ADAPTIVE

        self.vertical_alignment = ft.MainAxisAlignment.START
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.expand = True

        lista = []

        for i in range(20):
            lista.append(
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Text(
                                        value="12345"
                                    ),
                                    ft.Text(
                                        value="PERFUME X"
                                    )
                                ],
                                spacing=30
                            ),
                            ft.Text(
                                f"{i}x"
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        expand=True
                    ),
                    bgcolor=Colors.CINZA_CONTAINER,
                    border_radius=10,
                    shadow=ft.BoxShadow(
                        blur_radius=1,
                        color=Colors.VERDE_BOTI,
                        offset=ft.Offset(1, 3)
                    ),
                    height=60,
                    padding=ft.Padding.all(11)
                )
            )

        total_skus = len(lista)

        def print_comprovante(e):
            root_path = Path(__file__).parent.resolve()

            file_path = root_path / "upload" / "comprovantes" / "comp.pdf"
            file_path = str(re.sub(r"^envio[\\/].*$", "", file_path))

            print(file_path)

            if os.path.exists(file_path):
                os.startfile(filepath=file_path, operation="print")
                snackbar = ft.SnackBar(
                    content=ft.Text(
                        "Enviando para a impressora..."
                    )
                )
                page.show_dialog(snackbar)
                page.update()
            else:
                snackbar = ft.SnackBar(
                    content=ft.Text(value="Erro: Arquivo não encontrado!")
                )
                page.show_dialog(snackbar)
                page.update()


        self.controls = [

            ft.SafeArea(
                content=ft.Column(
                    controls=[
                        ft.Container(
                            content=Header(
                                title="Revisão",
                                steps=[3, 3],
                                page=page,
                                route="/send/insert"
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
                        ft.Container(height=10),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Row(
                                                controls=[
                                                    ft.Column(
                                                        controls=[
                                                            ft.Text(
                                                                value="ID DO BOLETO",
                                                                size=12,
                                                                color=ft.Colors.GREY
                                                            ),
                                                            ft.Text(
                                                                value="VC-992",
                                                                size=24,
                                                                color=Colors.VERDE_BOTI,
                                                                weight=ft.FontWeight.BOLD,
                                                                style=ft.TextStyle(
                                                                    letter_spacing=2
                                                                )
                                                            )
                                                        ]
                                                    ),
                                                    ft.Icon(
                                                        icon=ft.Icons.INBOX_OUTLINED,
                                                        color="#3B3A3A",
                                                        size=80,
                                                        opacity=0.5
                                                    )
                                                ],
                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            ),
                                            ft.Container(height=10),
                                            ft.Row(
                                                controls=[
                                                    ft.Column(
                                                        controls=[
                                                            ft.Text("ORIGEM"),
                                                            ft.Text(
                                                                value="Loja 4178",
                                                                weight=ft.FontWeight.BOLD,
                                                                style=ft.TextStyle(
                                                                    letter_spacing=2
                                                                )
                                                            )
                                                        ]
                                                    ),
                                                    ft.Icon(
                                                        icon=ft.Icons.ARROW_RIGHT_ROUNDED,
                                                        color=Colors.VERDE_BOTI,
                                                        size=40.001
                                                    ),
                                                    ft.Column(
                                                        controls=[
                                                            ft.Text("DESTINO"),
                                                            ft.Text(
                                                                value="Loja 4178",
                                                                weight=ft.FontWeight.BOLD,
                                                                style=ft.TextStyle(
                                                                    letter_spacing=2
                                                                )
                                                            )
                                                        ]
                                                    ),
                                                ],
                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                            )
                                        ]
                                    ),
                                    bgcolor=Colors.CINZA_CONTAINER,
                                    border_radius=10,
                                    shadow=ft.BoxShadow(
                                        blur_radius=2,
                                        color=Colors.ROXO_EUDORA,
                                        offset=ft.Offset(0, 3)
                                    ),
                                    # height=page.width * 0.4,
                                    width=page.width * 0.8,
                                    padding=ft.Padding.all(20),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            expand=True,
                        ),
                        ft.Container(height=10),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Row(
                                                controls=[
                                                    ft.Text(
                                                        value="MOVIMENTAÇÃO",
                                                        size=12,
                                                        color=ft.Colors.GREY,
                                                        text_align=ft.TextAlign.CENTER
                                                    )
                                                ],
                                                alignment=ft.MainAxisAlignment.CENTER
                                            ),
                                            ft.Row(
                                                controls=[
                                                    ft.Text(
                                                        value="REGULAR",
                                                        size=20,
                                                        color=ft.Colors.WHITE,
                                                        weight=ft.FontWeight.BOLD,
                                                    )
                                                ],
                                                alignment=ft.MainAxisAlignment.CENTER,
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    width=page.width * 0.35,
                                    bgcolor=Colors.CINZA_CONTAINER,
                                    border_radius=10,
                                    shadow=ft.BoxShadow(
                                        blur_radius=2,
                                        color=Colors.ROXO_EUDORA,
                                        offset=ft.Offset(0, 3)
                                    ),
                                    alignment=ft.Alignment.CENTER,
                                    padding=ft.Padding.all(5)
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Row(
                                                controls=[
                                                    ft.Text(
                                                        value="TOTAL DE ITENS",
                                                        size=12,
                                                        color=ft.Colors.GREY,
                                                        text_align=ft.TextAlign.CENTER
                                                    )
                                                ],
                                                alignment=ft.MainAxisAlignment.CENTER
                                            ),
                                            ft.Row(
                                                controls=[
                                                    ft.Text(
                                                        value="28",
                                                        size=20,
                                                        color=ft.Colors.WHITE,
                                                        weight=ft.FontWeight.BOLD,
                                                    )
                                                ],
                                                alignment=ft.MainAxisAlignment.CENTER,
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    width=page.width * 0.35,
                                    bgcolor=Colors.CINZA_CONTAINER,
                                    border_radius=10,
                                    shadow=ft.BoxShadow(
                                        blur_radius=2,
                                        color=Colors.ROXO_EUDORA,
                                        offset=ft.Offset(0, 3)
                                    ),
                                    alignment=ft.Alignment.CENTER,
                                    padding=ft.Padding.all(5),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                            height=page.height * 0.1,
                            expand=True,
                        ),
                        ft.Container(height=10),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Text("ITENS"),
                                    width=page.width * 0.3,
                                ),
                                ft.Container(
                                    content=ft.Text(
                                        f"{total_skus} SKUs",
                                        text_align=ft.TextAlign.END
                                    ),
                                    width=page.width * 0.3,
                                )
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Container(
                            content=ft.ListView(
                                controls=lista,
                                expand=True,
                                spacing=10,
                                padding=10,
                                width=page.width * 0.9,
                                # height=page.height * 0.35
                            ),
                            alignment=ft.Alignment.CENTER
                        ),
                        ft.Container(height=10),
                        ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.Icon(
                                        icon=ft.Icons.LOCAL_PRINTSHOP_ROUNDED,
                                        # size=30,
                                        color=ft.Colors.WHITE
                                    ),
                                    bgcolor=Colors.VERDE_BOTI,
                                    width=page.width * 0.2,
                                    on_click=print_comprovante
                                ),
                                ft.Button(
                                    content=ft.Row(
                                        controls=[
                                            ft.Text(
                                                value="CONFIRMAR",
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
                                    width=page.width * 0.6,
                                    height=40,
                                    on_click=lambda _ : page.run_task(page.push_route, "/")
                                )
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Container(height=10)
                    ],                
                ),
                expand=True,
            )

        ]