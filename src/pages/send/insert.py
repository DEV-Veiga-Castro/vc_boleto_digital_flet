import io
import logging
import time

from PIL import Image
from pyzbar.pyzbar import decode

import flet as ft
import flet_camera as fc

from components.camera import State, camera_label
from components.header import Header
from style.style import Colors

class SendItemsPage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.route = "/send/insert"

        self.image_counter = 0

        self.padding = 0
        self.spacing = 0

        self.bgcolor = Colors.BLACK_BACKGROUND

        self.scroll = ft.ScrollMode.ADAPTIVE

        self.vertical_alignment = ft.MainAxisAlignment.START
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.expand = True

        lista = []

        self.last_process_time = 0
        self.is_processing = False

        self.barcode_activated = False
        
        self.codigo_input = ft.TextField(
            value="",
            width=page.width * 0.7,
            border=ft.InputBorder.NONE,
            text_align=ft.TextAlign.CENTER,
            bgcolor=ft.Colors.TRANSPARENT,
            color=ft.Colors.BLACK,
            max_length=5,
            max_lines=1,
            margin=ft.Margin(
                bottom=2
            ),
            keyboard_type=ft.KeyboardType.NUMBER
        )

        self.barcode_switch = ft.Switch(
            value=self.barcode_activated,
            on_change=self.activate_reader,
            active_color=Colors.VERDE_BOTI,
            inactive_thumb_color=Colors.VERMELHO_OUI,
            thumb_icon=ft.Icons.CONTROL_CAMERA_ROUNDED
        )

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

        self.state = State()

        self.camera_control = fc.Camera(
            expand=True,
            preview_enabled=True,
            content=ft.Container(
                content=ft.Icon(
                    icon=ft.Icons.CENTER_FOCUS_STRONG,
                    color=ft.Colors.WHITE,
                    size=20
                )
            ),
            aspect_ratio=4/3,
            on_stream_image=self.on_streaming_image
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
                                "/send/initial"
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
                                    content=self.camera_control,
                                    height=180,
                                    width=page.width * 0.8,
                                    bgcolor=Colors.CINZA_CONTAINER,
                                    border_radius=20,
                                    alignment=ft.Alignment.CENTER,
                                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                )
                            ],
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Container(height=10),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=self.codigo_input,
                                    height=50,
                                    width=page.width * 0.65,
                                    bgcolor=ft.Colors.WHITE,
                                    border_radius=ft.BorderRadius.only(
                                        top_left=30,
                                        bottom_left=30
                                    ),
                                    alignment=ft.Alignment.CENTER,
                                ),
                                ft.Container(
                                    content=ft.Text(
                                        "+",
                                        color=ft.Colors.WHITE,
                                        size=30
                                    ),
                                    height=50,
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
                                height=page.height * 0.35
                            ),
                            alignment=ft.Alignment.CENTER
                        ),
                        # ft.Container(height=10)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True
                )
            )
        ]

        self.bottom_appbar = ft.BottomAppBar(
            content=ft.Row(
                controls=[
                    self.barcode_switch,
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
                        width=page.width * 0.6,
                        height=40,
                        on_click=lambda _ : page.run_task(page.push_route, "/send/revision")
                    )
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            bgcolor=ft.Colors.TRANSPARENT,
            height=60,
        )

        page.run_task(self.pre_fetch_cameras)

    async def get_cameras(self):
        self.state.cameras = await self.camera_control.get_available_cameras()
        self.state.camera_labels.clear()

        seen_labels: dict[str, int] = {}

        for camera in self.state.cameras:
            label = camera_label(camera)
            seen_labels[label] = seen_labels.get(label, 0) + 1
            if seen_labels[label] > 1:
                label = f"{label} ({seen_labels[label]})"
            self.state.camera_labels[camera.name] = label

        self.state.selected_camera = None
        self.state.is_initialized = False
        self.state.is_streaming = False
        self.state.is_recording = False
        self.state.is_recording_paused = False
        self.state.is_preview_paused = False
        self.state.is_streaming_supported = False
        self.state.device_orientation = None
        self.sync_camera_buttons()

        self.page.update()

    def sync_camera_buttons(self):
        self.barcode_switch.value = self.state.is_initialized

    async def pre_fetch_cameras(self):
        await self.get_cameras()

    async def start_streaming(self):
        if not self.state.is_initialized:
            await self.init_camera()

        self.page.update()

        if not self.state.is_streaming_supported:
            self.page.update()

            return False
        
        await self.camera_control.start_image_stream()
        self.state.is_streaming = True
        self.sync_camera_buttons()
        self.page.update()

    async def init_camera(self, e=None):
        if not self.state.cameras:
            return

        # Busca a câmera traseira de forma inteligente
        # Se não achar a 'BACK', ele pega a primeira da lista (0)
        self.state.selected_camera = next(
            (c for c in self.state.cameras if c.lens_direction == fc.CameraLensDirection.BACK),
            self.state.cameras[0]
        )

        if not self.state.selected_camera:
            return

        # Inicialização do hardware
        await self.camera_control.initialize(
            description=self.state.selected_camera,
            resolution_preset=fc.ResolutionPreset.HIGH,
            enable_audio=False,
            image_format_group=fc.ImageFormatGroup.JPEG
        )

        # Bloqueio de orientação (Essencial para APKs de logística/estoque)
        if not self.page.web:
            try:
                await self.camera_control.lock_capture_orientation()
            except Exception as ex:
                logging.warning(f"Não foi possível travar a orientação: {ex}")

        self.state.is_initialized = True
        
        # Inicia o streaming se suportado
        self.state.is_streaming_supported = await self.camera_control.supports_image_streaming()
        if self.state.is_streaming_supported:
            print("Suporto Streaming :)")
            await self.camera_control.start_image_stream()
            self.state.is_streaming = True
        
        self.sync_camera_buttons()
        self.page.update()

    async def activate_reader(self, e):
        self.barcode_activated = e.control.value 
        self.barcode_switch.thumb_icon = ft.Icons.CAMERA_ROUNDED if self.barcode_activated else ft.Icons.CONTROL_CAMERA_ROUNDED

        if self.barcode_activated:
            self.camera_control.visible = True
            self.page.update() # Força o Flet a renderizar o widget antes de tocar no hardware

            try:
                if self.state.is_initialized:
                    # Tenta o caminho mais rápido: Retomar
                    await self.camera_control.resume_preview()
                    if self.state.is_streaming_supported:
                        await self.camera_control.start_image_stream()
                        self.state.is_streaming = True
                else:
                    # Se nunca foi inicializado, faz o processo completo
                    await self.init_camera()
            
            except Exception as ex:
                # Se cair aqui (Ex: "Camera is not initialized"), 
                # ignoramos o estado antigo e forçamos um init do zero
                logging.error(f"Erro ao retomar câmera: {ex}. Reinicializando...")
                self.state.is_initialized = False 
                await self.init_camera()

        else:
            # Lógica de desligar (Safe Shutdown)
            if self.state.is_initialized:
                try:
                    if self.state.is_streaming:
                        await self.camera_control.stop_image_stream()
                        self.state.is_streaming = False
                    
                    await self.camera_control.pause_preview()
                except Exception as ex:
                    logging.warning(f"Erro ao pausar (talvez já estivesse pausada): {ex}")
                
                self.camera_control.visible = False
        
        self.page.update()

    async def on_streaming_image(self, e: fc.CameraImageEvent):
        self.image_counter += 1
        print(f"Streaming a Image --- {self.image_counter}")

        current_time = time.time()

        if current_time - self.last_process_time < 0.6 or self.is_processing:
            return
        
        self.is_processing = True

        try:
            img = Image.open(io.BytesIO(e.bytes))

            img = img.convert("L")
            
            barcodes = decode(img)

            for barcode in barcodes:
                barcode_data = barcode.data.decode("utf-8")

                if barcode_data:
                    await self.on_barcode_scanner(barcode_data)
                    break
        except Exception as ex:
            print(f"Erro no processamento pyzbar: {ex}")
        finally:
            self.last_process_time = time.time()
            self.is_processing = False

    async def on_barcode_scanner(self, value):
        print(f"Código: {value} - Tamanho: {len(value)}")
        value = value[7:]
        value = value[:5]
        print(f"Código Reduzido: {value} - Tamanho: {len(value)}")
        self.codigo_input.value = value
        self.codigo_input.update()