from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from fastapi_snowflake_challenge.schemas.client import ClientSchema
from fastapi_snowflake_challenge.models.client import Client
from fastapi_snowflake_challenge.services.db import get_session_depends

router = APIRouter(
    prefix="/clients",
    tags=["clients"],
)


@router.post("/", response_model=ClientSchema)
async def create_client(client: ClientSchema, db_session: Session = Depends(get_session_depends)):
    if Client.exists(db_session, client.email):
        raise HTTPException(status_code=400, detail="Client with this email already exists.")

    return Client.create(db_session, client)


@router.get("/", response_model=list[ClientSchema])
async def get_clients(db_session: Session = Depends(get_session_depends)):
    return db_session.query(Client).all()


@router.get("/{client_id}", response_model=ClientSchema)
async def get_client_details(client_id: int, db_session: Session = Depends(get_session_depends)):
    client = Client.get(db_session, client_id)
    if client is None:
        raise HTTPException(status_code=404, detail=f"Client not found with id {client_id}")
    return client


@router.put("/{client_id}", response_model=ClientSchema)
async def update_client(client_id: int, client: ClientSchema, db_session: Session = Depends(get_session_depends)):
    if Client.exists(db_session, client.email):
        raise HTTPException(status_code=400, detail="Client with this email already exists.")

    client = Client.update(db_session, client_id, client)
    if client is None:
        raise HTTPException(status_code=404, detail=f"Client not found with id {client_id}")
    return client


@router.delete("/{client_id}", status_code=204)
async def delete_client(client_id: int, db_session: Session = Depends(get_session_depends)):
    deleted = Client.delete(db_session, client_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Client not found with id {client_id}")
