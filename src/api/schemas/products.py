from typing import Dict, Optional

from pydantic import BaseModel

class Category(BaseModel):
    id: int
    name: str
    percentual_desconto: Optional[float] = 0.0

class Produto(BaseModel):
    cod_product: int
    description: str
    price: Optional[float] = 0.0
    category: Optional[dict] 

    is_active: bool = True
    created_at: Optional[str] = ""
    updated_at: Optional[str] = ""