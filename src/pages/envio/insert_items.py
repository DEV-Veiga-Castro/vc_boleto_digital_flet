import flet as ft
import flet_camera as fc

from components.header import Header
from style.style import Colors

class InsertItems(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.route = "/insert_items_envio"

        self.padding = 0
        self.spacing = 0

        self.scroll = ft.ScrollMode.ADAPTIVE

        self.vertical_alignment = ft.MainAxisAlignment.START
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.expand = True

        lista = []

        self.barcode_activated = False
        self.barcode_color = Colors.VERMELHO_OUI

        self.barcode_button = ft.IconButton(
            icon=ft.Icon(
                icon=ft.Icons.BARCODE_READER,
                color=ft.Colors.WHITE,
                size=20
            ),
            bgcolor=self.barcode_color,
            on_click=lambda e: activate_reader(self, e),
            width=page.width * 0.1,
            # height=40,
            alignment=ft.Alignment.CENTER
        )

        def activate_reader(self, e):
            self.barcode_activated = not self.barcode_activated
            self.barcode_button.bgcolor = Colors.VERDE_BOTI if self.barcode_activated else Colors.VERMELHO_OUI

            page.update()


        for i in range(100):
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
                    border_radius=15,
                    shadow=ft.BoxShadow(
                        blur_radius=1,
                        color=Colors.VERDE_BOTI,
                        offset=ft.Offset(1, 3)
                    ),
                    height=40,
                    padding=ft.Padding.all(11)
                )
            )

        self.controls = [
            ft.SafeArea(
                content=ft.Column(
                    controls=[
                        ft.Container(
                            content=Header(
                                "Inserção de Itens", 
                                [2, 3], 
                                page, 
                                "/initial_config_envio"
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
                                    content=ft.Text("Camera"),
                                    height=180,
                                    width=page.width * 0.8,
                                    bgcolor=Colors.CINZA_CONTAINER,
                                    border_radius=20,
                                    alignment=ft.Alignment.CENTER
                                )
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Container(height=10),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Text("INPUT"),
                                    height=40,
                                    width=page.width * 0.65,
                                    bgcolor=Colors.CINZA_CONTAINER,
                                    border_radius=ft.BorderRadius.only(
                                        top_left=30,
                                        bottom_left=30
                                    ),
                                    alignment=ft.Alignment.CENTER
                                ),
                                ft.Container(
                                    content=ft.Text(
                                        "+",
                                        color=ft.Colors.WHITE,
                                        size=30
                                    ),
                                    height=40,
                                    width=page.width * 0.15,
                                    bgcolor=Colors.VERDE_BOTI,
                                    border_radius=ft.BorderRadius.only(
                                        top_right=30,
                                        bottom_right=30
                                    ),
                                    alignment=ft.Alignment.CENTER
                                )
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=0
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
                                        f"{'X'} SKUs",
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
                                width=page.width * 0.8,
                                height=page.height * 0.35
                            ),
                            alignment=ft.Alignment.CENTER
                        ),
                        ft.Container(height=10)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True
                )
            )
        ]

        self.bottom_appbar = ft.BottomAppBar(
            content=ft.Row(
                controls=[
                    self.barcode_button,
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
                        width=page.width * 0.5,
                        height=40,
                        on_click=lambda _ : page.run_task(page.push_route, "/insert_items_envio")
                    )
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            bgcolor=ft.Colors.TRANSPARENT
        )
