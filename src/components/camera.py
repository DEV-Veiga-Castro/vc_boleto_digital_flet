from dataclasses import dataclass, field
from typing import List

import flet_camera as fc
import flet as ft

@dataclass
class State:
    cameras: List[fc.CameraDescription] = field(default_factory=list)
    selected_camera: fc.CameraDescription | None = None
    camera_labels: dict[str, str] = field(default_factory=dict)
    is_streaming: bool = False
    is_streaming_supported: bool = False
    is_initialized: bool = False
    is_preview_paused: bool = False
    is_recording: bool = False
    is_recording_paused: bool = False
    device_orientation: ft.DeviceOrientation | None = None


def has_readable_name(camera: fc.CameraDescription) -> bool:
    name = camera.name.strip()

    if not name:
        return False
    if name.startswith("com.apple.avfoundation."):
        return False
    
    return not (":" in name and "." in name)

def camera_label(camera: fc.CameraDescription) -> str:
    if has_readable_name(camera):
        return camera.name

    direction = camera.lens_direction.value.capitalize()

    lens_map = {
        "wide": "Wide",
        "telephoto": "Telephoto",
        "ultraWide": "Ultra Wide",
        "unknown": "Unknown",
    }

    lens_type = lens_map.get(camera.lens_type.value, camera.lens_type.value)

    return f"{direction} ({lens_type})"

def device_orientation_degress(orientation: ft.DeviceOrientation | None) -> int:
    if orientation == ft.DeviceOrientation.PORTRAIT_UP:
        return 0
    if orientation == ft.DeviceOrientation.LANDSCAPE_RIGHT:
        return 90
    if orientation == ft.DeviceOrientation.PORTRAIT_DOWN:
        return 180
    if orientation == ft.DeviceOrientation.LANDSCAPE_LEFT:
        return 270
    return 0