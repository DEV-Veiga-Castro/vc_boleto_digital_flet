import requests
from api.schemas.products import Produto
from appstate import AppState
from config import Config

state: AppState = AppState()

async def list_products():
    r = requests.request("GET", url=f"{Config.API_URL}/product")

    r = r.json()

    data = [Produto(**item) for item in r]

    state.product_list = data

    print(state.product_list[next(i for i, item in enumerate(state.product_list) if item[state.product_list[i].cod_product] == 1314)].description)

        

