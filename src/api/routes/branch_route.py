from typing import List

import requests
import flet as ft

from api.schemas.branch import Branch
from config import Config

async def list_branchs(access_token: str) -> List:

    if not access_token:
        print("Sem token")
        return []

    r = requests.request(
        method="GET",
        url=f"{Config.API_URL}/branch/",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    if r.status_code == 200:
        data = r.json()

        branches = [Branch.model_validate(i) for i in data]

        return branches
    
    elif r.status_code == 401:
        return False