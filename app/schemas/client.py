from typing import Optional

from pydantic import BaseModel, EmailStr


class ClientBase(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None


class ClientCreate(ClientBase):
    name: str
    email: EmailStr


class ClientUpdate(ClientBase):
    pass
