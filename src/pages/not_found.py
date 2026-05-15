import flet as ft

class NotFoundPage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.route = "/404"

        self.padding = 0
        self.spacing = 0

        self.vertical_alignment = ft.MainAxisAlignment.START
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.controls = [
            ft.SafeArea(
                content=ft.Stack(
                    controls=[
                        ft.Image(
                            src="images/not_found_gif.gif",
                            width=page.width,
                            height=page.height,
                            fit=ft.BoxFit.CONTAIN
                        ),
                        ft.Row(
                            controls=[
                                ft.Text(
                                    value="ERROR: 404",
                                    color=ft.Colors.WHITE,
                                    size=40,
                                    weight=ft.FontWeight.BOLD,
                                    opacity=0.5,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            controls=[
                                ft.Text(
                                    value="Página não encontrada!",
                                    color=ft.Colors.WHITE,
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    opacity=0.5,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            margin=ft.Margin(
                                top=50
                            )
                        )
                    ]
                )
            )
        ]