from sqlalchemy.orm import Session

from app.tables.client import Client
from app.schemas.client import ClientCreate, ClientUpdate


def create_client(db: Session, client: ClientCreate):
    db_client = Client(name=client.name, email=client.email)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def get_client(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()


def update_client(db: Session, client_id: int, client: ClientUpdate):
    client = get_client(db, client_id)
    if client:
        for key, value in client.dict(exclude_unset=True).items():
            setattr(client, key, value)
        db.commit()
        db.refresh(client)
    return client


def delete_client(db: Session, client_id: int):
    db_client = get_client(db, client_id)
    if db_client:
        db.delete(db_client)
        db.commit()
        return True
    return False
