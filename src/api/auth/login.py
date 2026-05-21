import flet as ft

from requests import request

from config import Config

async def auth_login(page: ft.Page, login: str, password: str):

    r = request(
        method="POST",
        url=f"{Config.API_URL}/auth/login",
        json={
            "login": login,
            "password": password
        }
    )

    return r