from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    username: str
    name: str
    surname: str
    email: EmailStr
    data_nascimento: str
    cpf: str
    is_active: bool
    is_validated: bool
    is_admin: bool
    role: dict = {"id": int, "name": str}
    branch: list = [
        {
            "pdv": int,
            "name": str,
            "address": str,
            "phone": str,
            "city": str,
            "state": str,
            "cnpj": str,
            "is_active": bool
        }
    ]
    