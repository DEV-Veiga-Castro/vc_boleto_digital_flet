from typing import Optional

from pydantic import BaseModel

class Branch(BaseModel):
    pdv: int
    name: str
    address: str
    phone: Optional[str] = None
    city: str
    state: str
    cnpj: str
    is_active: bool