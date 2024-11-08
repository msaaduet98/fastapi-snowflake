from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.routes.crud import *
from app.db.database import get_db
from app.schemas.client import ClientCreate, ClientUpdate

from app.tables.client import Client
from app.config import DATABASE_URL


router = APIRouter()


@router.post("/clients", response_model=dict)
async def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    return create_client(db=db, client=client)


@router.get("/clients", response_model=dict)
async def get_all_clients(client: ClientCreate, db: Session = Depends(get_db)):
    return create_client(db=db, client=client)


@router.get("/clients/{client_id}", response_model=dict)
async def get_client(client_id: int, db: Session = Depends(get_db)):
    from pdb import set_trace; set_trace()
    client = get_client(db, client_id=client_id)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client


@router.put("/clients/{client_id}", response_model=dict)
async def update_client(client_id: int, client: ClientUpdate, db: Session = Depends(get_db)):
    client = update_client(db=db, client_id=client_id, client=client)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client


@router.delete("/clients/{client_id}", status_code=204)
async def delete_client(client_id: int, db: Session = Depends(get_db)):
    deleted = delete_client(db=db, client_id=client_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Client not found")
