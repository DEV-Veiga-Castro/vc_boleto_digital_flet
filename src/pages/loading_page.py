import flet as ft

def loading_page(page: ft.Page):
    body = ft.SafeArea(
        expand=True,
        content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Image(
                                    src="images/logo_preta.png",
                                    width=150,
                                    height=150,
                                    align=ft.Alignment.CENTER,
                                ),
                                ft.Image(
                                    src="images/loading.gif",
                                    width=120,
                                    height=120,
                                    align=ft.Alignment.CENTER
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=50
                        ),
                        expand=True,
                        alignment=ft.Alignment.CENTER,
                    ),
                ],
            )
    )

    return body