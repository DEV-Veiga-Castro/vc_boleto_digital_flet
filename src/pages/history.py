import datetime

import flet as ft

from style.style import Colors

class HistoryPage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.route = "/history"

        self.spacing = 0
        self.padding = 0

        self.bgcolor = Colors.BLACK_BACKGROUND

        self.scroll = ft.ScrollMode.ADAPTIVE

        self.vertical_alignment = ft.MainAxisAlignment.START
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.expand = True

        self.picker = ft.DatePicker(
            on_change=self.on_date_changed,
            on_dismiss=self.on_date_cancel,
            locale=ft.Locale(
                language_code="pt",
                country_code="BR"
            )
        )

        # page.overlay.append(self.picker)

        self.data_inicio = datetime.date.today()
        self.text_inicio = ft.TextField(
                                value=self.data_inicio.strftime("%d/%m/%Y"),
                                border=ft.InputBorder.NONE,
                                keyboard_type=ft.KeyboardType.DATETIME,
                                bgcolor=ft.Colors.TRANSPARENT,
                                text_align=ft.TextAlign.CENTER,
                                width=page.width * 0.4,
                                color=ft.Colors.WHITE,
                                hover_color=ft.Colors.TRANSPARENT,
                                on_click=self.select_date_inicio,
                                read_only=True
                            )

        self.data_fim = datetime.date.today()
        self.text_fim = ft.TextField(
                            value=self.data_fim.strftime("%d/%m/%Y"),
                            border=ft.InputBorder.NONE,
                            keyboard_type=ft.KeyboardType.DATETIME,
                            bgcolor=ft.Colors.TRANSPARENT,
                            text_align=ft.TextAlign.CENTER,
                            width=page.width * 0.4,
                            color=ft.Colors.WHITE,
                            hover_color=ft.Colors.TRANSPARENT,
                            on_click=self.select_date_fim,
                            read_only=True
                        )
        
        self.current_date_picker = None
        
        self.num_boleto = ""

        self.lista_transferencias = []

        for i in range(10):
            self.lista_transferencias.append(
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        value="VC-001",
                                        color=ft.Colors.WHITE,
                                        size=16,
                                        weight=ft.FontWeight.W_500
                                    ),
                                    ft.Text(
                                        value="Loja Origem: 4178",
                                        color=ft.Colors.GREY,
                                        size=12
                                    ),
                                    ft.Text(
                                        value="Data",
                                        color=ft.Colors.GREY,
                                        size=12
                                    )
                                ],
                                spacing=2
                            ),
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        value="REGULAR",
                                        color=ft.Colors.WHITE,
                                        size=16,
                                        weight=ft.FontWeight.W_500,
                                    ),
                                    ft.Container(height=10),
                                    ft.Container(height=10)
                                ],
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    bgcolor=Colors.CINZA_CONTAINER,
                    border_radius=10,
                    padding=20
                )
            )

        self.controls = [
            ft.SafeArea(
                content=ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.AppBar(
                                    bgcolor=ft.Colors.TRANSPARENT,
                                    leading=ft.IconButton(
                                        icon=ft.Icon(
                                            icon=ft.Icons.ARROW_BACK_IOS_ROUNDED,
                                            color=ft.Colors.WHITE
                                        ),
                                        on_click=lambda _ : page.run_task(page.push_route, "/")
                                    ),
                                    title=ft.Text(
                                        value="Histórico",
                                        size=24,
                                        color=ft.Colors.WHITE,
                                        weight=ft.FontWeight.W_500,
                                        style=ft.TextStyle(
                                            letter_spacing=5
                                        )
                                    ),
                                    actions=[
                                        ft.IconButton(
                                            icon=ft.Icons.QUESTION_MARK_ROUNDED,
                                            icon_color=ft.Colors.WHITE,
                                            margin=ft.Margin(
                                                right=10
                                            )
                                        )
                                    ]                            
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
                                shadow=ft.BoxShadow(
                                    spread_radius=-10,
                                    blur_radius=15,
                                    color="#808080"
                                ),
                                border_radius=ft.BorderRadius(
                                    top_left=0,
                                    top_right=0,
                                    bottom_left=30,
                                    bottom_right=30
                                )
                        ),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Row(
                                                controls=[
                                                    ft.Text(
                                                        value="Data Inicial",
                                                        color=ft.Colors.GREY
                                                    )
                                                ],
                                                margin=ft.Margin(
                                                    left=10,
                                                    top=5
                                                )
                                            ),
                                            ft.Row(
                                                controls=[
                                                    self.text_inicio
                                                ],
                                                alignment=ft.Alignment.CENTER
                                            ),
                                            ft.Container(
                                                height=10
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        expand=True,
                                        spacing=2
                                    ),
                                    bgcolor=Colors.CINZA_CONTAINER,
                                    border_radius=10,
                                    shadow=ft.BoxShadow(
                                        blur_radius=2,
                                        color=Colors.VERDE_BOTI,
                                        offset=ft.Offset(0, 3)
                                    ),
                                    width=page.width * 0.4,
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Row(
                                                controls=[
                                                    ft.Text(
                                                        value="Data Final",
                                                        color=ft.Colors.GREY
                                                    )
                                                ],
                                                margin=ft.Margin(
                                                    left=10,
                                                    top=5
                                                )
                                            ),
                                            ft.Row(
                                                controls=[
                                                    self.text_fim
                                                ],
                                                alignment=ft.Alignment.CENTER
                                            ),
                                            ft.Container(
                                                height=10
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        expand=True,
                                        spacing=2
                                    ),
                                    bgcolor=Colors.CINZA_CONTAINER,
                                    border_radius=10,
                                    shadow=ft.BoxShadow(
                                        blur_radius=2,
                                        color=Colors.VERDE_BOTI,
                                        offset=ft.Offset(0, 3)
                                    ),
                                    width=page.width * 0.4
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                            margin=ft.Margin(
                                top=20
                            )
                        ),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.TextField(
                                        value=self.num_boleto,
                                        border=ft.InputBorder.NONE,
                                        margin=ft.Margin(
                                            left=10
                                        ),
                                        color=ft.Colors.WHITE,
                                        text_align=ft.TextAlign.CENTER,
                                        bgcolor=ft.Colors.TRANSPARENT,
                                        hint_text="Número do Boleto",
                                        hover_color=ft.Colors.TRANSPARENT,
                                        keyboard_type=ft.KeyboardType.NUMBER
                                    ),
                                    bgcolor=Colors.CINZA_CONTAINER,
                                    border_radius=ft.BorderRadius.only(
                                        top_left=10,
                                        bottom_left=10
                                    ),
                                    shadow=ft.BoxShadow(
                                        blur_radius=2,
                                        color=Colors.VERDE_BOTI,
                                        offset=ft.Offset(0, 3)
                                    ),
                                    height=50,
                                    width=page.width * 0.75,
                                ),
                                ft.Container(
                                    content=ft.IconButton(
                                        icon=ft.Icons.FILTER_LIST_ROUNDED,
                                        icon_color=ft.Colors.WHITE,
                                        icon_size=30,
                                        alignment=ft.Alignment.CENTER
                                    ),
                                    bgcolor=Colors.VERDE_BOTI,
                                    border_radius=ft.BorderRadius(
                                        top_left=0,
                                        top_right=10,
                                        bottom_left=0,
                                        bottom_right=10
                                    ),
                                    alignment=ft.Alignment.CENTER,
                                    height=50,
                                    shadow=ft.BoxShadow(
                                        blur_radius=2,
                                        color=Colors.VERDE_BOTI,
                                        offset=ft.Offset(0, 3)
                                    ),
                                    width=page.width * 0.13
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=0,
                            margin=ft.Margin(
                                top=20
                            )
                        ),
                        ft.Container(height=10),
                        ft.Container(
                            content=ft.ListView(
                                controls=self.lista_transferencias,
                                expand=True,
                                spacing=10,
                                padding=10,
                                width=page.width * 0.9,
                                height=page.height * 0.6
                            ),
                            alignment=ft.Alignment.CENTER
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True
                ),
                expand=True
            )
        ]

        page.update()

    async def select_date_inicio(self, e):
        self.current_date_picker = "inicio"
        self.picker.value = self.data_inicio
        self.picker.open = True

        self.page.show_dialog(self.picker)


    async def select_date_fim(self, e):
        self.current_date_picker = "fim"
        self.picker.value = self.data_fim
        self.picker.open = True

        self.page.show_dialog(self.picker)

    async def on_date_changed(self, e):
        if not self.picker.value:
            return
        
        selected_date = self.picker.value.date() if hasattr(self.picker.value, "date") else self.picker.value

        if self.current_date_picker == "inicio":
            self.data_inicio = selected_date
            self.text_inicio.value = self.data_inicio.strftime("%d/%m/%Y")
            self.text_inicio.update()
            
        else:
            self.data_fim = selected_date
            self.text_fim.value = self.data_fim.strftime("%d/%m/%Y")
            self.text_fim.update()

        self.picker.open = False

    async def on_date_cancel(self, e):
        self.current_date_picker = None
        self.picker.open = False