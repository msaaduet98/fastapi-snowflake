from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.crud import client_crud
from app.db.database import get_db
from app.schemas.client import ClientCreate, ClientUpdate


router = APIRouter()


@router.post("/clients", response_model=dict)
async def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    return client_crud.create_client(db=db, client=client)


@router.get("/clients/{client_id}", response_model=dict)
async def get_client(client_id: int, db: Session = Depends(get_db)):
    db_client = client_crud.get_client(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client


@router.put("/clients/{client_id}", response_model=dict)
async def update_client(client_id: int, client: ClientUpdate, db: Session = Depends(get_db)):
    db_client = client_crud.update_client(db=db, client_id=client_id, client=client)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client


@router.delete("/clients/{client_id}", status_code=204)
async def delete_client(client_id: int, db: Session = Depends(get_db)):
    deleted = client_crud.delete_client(db=db, client_id=client_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Client not found")
