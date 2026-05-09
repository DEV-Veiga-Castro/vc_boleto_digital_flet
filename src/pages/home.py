import flet as ft
import flet_camera as fc

from style.style import Colors

class HomePage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "/"

        self.padding = 0
        self.spacing = 0

        self.scroll = ft.ScrollMode.ADAPTIVE

        # self.align = ft.MainAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.START
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.expand = True

        self.controls = [
            ft.Container(
                content=ft.AppBar(
                    leading=ft.IconButton(
                        icon=ft.Image(
                            src="images/logo_preta.png",
                            width=60,
                            height=60
                        ),
                        padding=ft.Padding(
                            left=10
                        ),
                        expand=True
                    ),
                    title=ft.Column(
                        controls=[
                            ft.Text(
                                value="Olá,",
                                size=16,
                                color=ft.Colors.WHITE
                            ),
                            ft.Text(
                                value="Usuário!"
                            )
                        ],
                        spacing=1
                    ),
                    actions=[
                        ft.IconButton(
                            icon=ft.Icon(
                                ft.Icons.HISTORY_SHARP,
                                badge=ft.Badge()
                            ),
                            tooltip="Histórico",
                            margin=ft.Margin(
                                right=10
                            ),
                            icon_size=30,
                            icon_color=ft.Colors.WHITE,
                        )
                    ],
                    expand=True,
                    bgcolor=ft.Colors.TRANSPARENT,
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
                                ft.Icon(
                                    icon=ft.Icons.SWIPE_UP_OUTLINED,
                                    color=Colors.VERDE_BOTI,
                                    size=80,
                                    margin=ft.Margin(
                                        left=20
                                    )
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Container(
                                            content=ft.Text(
                                                value="Enviar",
                                                color=ft.Colors.WHITE,
                                                size=24,
                                            ),
                                            alignment=ft.Alignment.CENTER,
                                        ),
                                        ft.Container(
                                            content=ft.Text(
                                                value="Movimentação",
                                                color=ft.Colors.WHITE,
                                                size=24,
                                            ),
                                            alignment=ft.Alignment.CENTER
                                        )
                                    ],
                                    alignment=ft.CrossAxisAlignment.CENTER,
                                    expand=True,
                                    spacing=1
                                )
                            ],
                        ),
                        bgcolor=Colors.CINZA_CONTAINER,
                        height=180,
                        width=page.width * 0.8,
                        border_radius=20,
                        shadow=ft.BoxShadow(
                            blur_radius=2,
                            color=Colors.VERDE_BOTI,
                            offset=ft.Offset(2, 4)
                        ),
                        alignment=ft.Alignment.CENTER
                    )
                ],
                margin=ft.Margin(
                    top=40
                ),
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Icon(
                                    icon=ft.Icons.SWIPE_DOWN_OUTLINED,
                                    color=Colors.VERDE_BOTI,
                                    size=80,
                                    margin=ft.Margin(
                                        left=20
                                    )
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Container(
                                            content=ft.Text(
                                                value="Receber",
                                                color=ft.Colors.WHITE,
                                                size=24,
                                            ),
                                            alignment=ft.Alignment.CENTER,
                                        ),
                                        ft.Container(
                                            content=ft.Text(
                                                value="Movimentação",
                                                color=ft.Colors.WHITE,
                                                size=24,
                                            ),
                                            alignment=ft.Alignment.CENTER
                                        )
                                    ],
                                    alignment=ft.CrossAxisAlignment.CENTER,
                                    expand=True,
                                    spacing=1
                                )
                            ],
                        ),
                        bgcolor=Colors.CINZA_CONTAINER,
                        height=180,
                        width=page.width * 0.8,
                        border_radius=20,
                        shadow=ft.BoxShadow(
                            blur_radius=2,
                            color=Colors.VERDE_BOTI,
                            offset=ft.Offset(2, 4)
                        ),
                        alignment=ft.Alignment.CENTER
                    )
                ],
                margin=ft.Margin(
                    top=40
                ),
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[

                                ft.Container(
                                    content=ft.Text(
                                        value="EM TRÂNSITO",
                                        size=12,
                                        weight=ft.FontWeight.BOLD,
                                        text_align=ft.TextAlign.CENTER
                                    ),
                                    alignment=ft.Alignment.TOP_CENTER
                                ),

                                ft.Container(
                                    content=ft.Text(
                                        value="14",
                                        size=32,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    expand=True,
                                    alignment=ft.Alignment.CENTER
                                ),

                                ft.Container(
                                    height=12
                                )
                            ],
                            spacing=0,
                            alignment=ft.MainAxisAlignment.START
                        ),
                        bgcolor=Colors.CINZA_CONTAINER,
                        height=140,
                        width=page.width * 0.35,
                        border_radius=20,
                        padding=10,
                        shadow=ft.BoxShadow(
                            blur_radius=2,
                            color=Colors.VERDE_BOTI,
                            offset=ft.Offset(2, 4)
                        ),
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[

                                ft.Container(
                                    content=ft.Text(
                                        value="RECEBIDAS",
                                        size=12,
                                        weight=ft.FontWeight.BOLD,
                                        text_align=ft.TextAlign.CENTER
                                    ),
                                    alignment=ft.Alignment.TOP_CENTER
                                ),

                                ft.Container(
                                    content=ft.Text(
                                        value="14",
                                        size=32,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    expand=True,
                                    alignment=ft.Alignment.CENTER
                                ),

                                ft.Container(
                                    height=12
                                )
                            ],
                            spacing=0,
                            alignment=ft.MainAxisAlignment.START
                        ),
                        bgcolor=Colors.CINZA_CONTAINER,
                        height=140,
                        width=page.width * 0.35,
                        border_radius=20,
                        padding=10,
                        shadow=ft.BoxShadow(
                            blur_radius=2,
                            color=Colors.VERDE_BOTI,
                            offset=ft.Offset(2, 4)
                        ),
                    ),
                ],
                margin=ft.Margin(
                    top=40
                ),
                expand=True,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                width=page.width * 0.8,
                spacing=40
            ),
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Image(
                            src="images/logo_custom.png",
                            height=30
                        )
                    )
                ],
                expand=True,
                margin=ft.Margin(
                    top=40
                ),
                alignment=ft.MainAxisAlignment.CENTER
            )
        ]
