import flet as ft

class TestPage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "/test"

        self.spacing = 0
        self.padding = 0

        self.scroll = ft.ScrollMode.ADAPTIVE

        self.vertical_alignment = ft.MainAxisAlignment.START
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.expand = True

        # 1. Componentes Fixos: AppBar
        self.appbar = ft.AppBar(
            title=ft.Text("Meu App"),
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            center_title=True,
        )

        # 2. As telas que vão deslizar (as "Páginas")
        self.tela_1 = ft.Column(
            controls=[ft.Text(value="Tela de Início", size=30, weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE)]
        )

        self.tela_2 = ft.Container(
            content=ft.Text(value="Tela de Estoque / Filtros", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
        )

        self.tela_3 = ft.Container(
            content=ft.Column([
                ft.Text(value="Tela de Configurações", size=30, weight=ft.FontWeight.BOLD),
                ft.Text(value="⬅️ Arraste para a direita", size=16),
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            bgcolor=ft.Colors.WHITE,
            expand=True
        )

        # 3. O gerenciador do Swiping (PageView)
        self.view_paginas = ft.PageView(
            expand=True,  # Ocupa todo o espaço entre a AppBar e a BottomAppBar
            controls=[self.tela_1, self.tela_2, self.tela_3],
            on_change=self.on_page_changed # Dispara quando o usuário arrasta
        )

        # 4. Componentes Fixos: BottomAppBar (ou NavigationBar)
        self.nav_bar = ft.NavigationBar(
            selected_index=0,
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Início"),
                ft.NavigationBarDestination(icon=ft.Icons.REORDER, label="Filtros"),
                ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Ajustes"),
            ],
            on_change=self.on_nav_click
        )
        self.navigation_bar = self.nav_bar

        # O conteúdo principal da View será APENAS o PageView
        self.controls = [self.view_paginas]

    async def on_page_changed(self, e):
        """Sincroniza a Bottom Bar quando o usuário arrasta a tela"""
        # e.data traz o índice da página atual (0, 1, 2...) como string
        self.nav_bar.selected_index = int(e.data)
        self.nav_bar.update()

    async def on_nav_click(self, e):
        """Sincroniza a tela quando o usuário clica nos botões da Bottom Bar"""
        target_page = e.control.selected_index
        
        # Faz a transição visual saltar para a página clicada
        self.view_paginas.selected_index = target_page
        self.view_paginas.update()