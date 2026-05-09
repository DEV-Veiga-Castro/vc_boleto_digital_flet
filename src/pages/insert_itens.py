import flet as ft
import flet_camera as fc

class SendPage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        
        self.route = "/send"

        self.padding = 0
        self.spacing = 0

        self.controls = [
            ft.SafeArea(
                expand=True,
                content=ft.Column(
                    controls=[
                        ft.AppBar(
                            leading=ft.IconButton(
                                icon=ft.Icons.ARROW_BACK_IOS_ROUNDED,
                                on_click=lambda e: page.run_task(page.push_route, "/")
                            ),
                            title=ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Text(
                                            value="PASSO 02 DE 03",
                                            size=16,
                                            color=ft.Colors.WHITE
                                        ),
                                        ft.Text(
                                            value="Inserção de Itens",
                                            size=24,
                                            color=ft.Colors.WHITE   
                                        )
                                    ]
                                )
                            ),
                            actions=[
                                ft.Container(
                                    content=ft.Row(
                                        controls=[
                                            ft.Container(
                                                content=ft.Text(" "),
                                                bgcolor=ft.Colors.WHITE,
                                                width=20,
                                                height=10,
                                                border_radius=30
                                            ),
                                            ft.Container(
                                                content=ft.Text(" "),
                                                bgcolor=ft.Colors.GREEN,
                                                width=40,
                                                height=10,
                                                border_radius=30
                                            ),
                                            ft.Container(
                                                content=ft.Text(" "),
                                                bgcolor=ft.Colors.WHITE,
                                                width=20,
                                                height=10,
                                                border_radius=30
                                            )
                                        ],
                                        spacing=2
                                    )
                                )
                            ],
                        )
                    ]
                )
            )
        ]
