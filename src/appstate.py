from typing import List

from api.schemas.products import Produto


class AppState:
    _isinstace = None

    def __new__(cls):
        if cls._isinstace is None:
            cls._isinstace = super(AppState, cls).__new__(cls)

            cls._isinstace.product_list: List[Produto] = []

        return cls._isinstace



