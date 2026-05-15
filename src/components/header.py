from typing import List

import flet as ft

from style.style import Colors

class Header(ft.AppBar):
    def __init__(self, title: str, steps: List[int], page: ft.Page, route: str):
        super().__init__()

        step_1 = steps[0]
        step_2 = steps[1]

        container_actions = []

        def render_actions():
            for i in range(step_2):
                if i + 1 == step_1:
                    container_actions.append(
                        ft.Container(
                            content=ft.Text(""),
                            bgcolor=Colors.VERDE_BOTI, # Branco - Não Tela Atual || Verde - Tela Atual
                            width=40, # 40 caso seja a tela atual - 20 caso não
                            height=10,
                            border_radius=30
                        )
                    )
                else:
                    container_actions.append(
                        ft.Container(
                            content=ft.Text(""),
                            bgcolor=ft.Colors.WHITE, # Branco - Não Tela Atual || Verde - Tela Atual
                            width=20, # 40 caso seja a tela atual - 20 caso não
                            height=10,
                            border_radius=30
                        )
                    )

        render_actions()

        self.bgcolor=ft.Colors.TRANSPARENT

        self.leading=ft.IconButton(
            icon=ft.Icon(
                icon=ft.Icons.ARROW_BACK_IOS_ROUNDED,
                color=ft.Colors.WHITE
            ),
            on_click=lambda _ : page.run_task(page.push_route, route) 
        )
                
        self.title=ft.Column(
            controls=[
                ft.Text(
                    value=f"PASSO 0{step_1} de 0{step_2}",
                    size=16,
                    color=ft.Colors.WHITE
                ),
                ft.Text(
                    value=title,
                    size=24,
                    color=ft.Colors.WHITE
                )
            ]
        )
        self.actions=[
            ft.Container(
                content=ft.Row(
                    controls=container_actions,
                    spacing=2
                ),
                padding=ft.Padding(
                    right=15
                )
            )
        ]

        page.update()
    

