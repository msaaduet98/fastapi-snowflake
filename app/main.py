from fastapi import FastAPI
from app.api import clients
from app.db.database import engine, Base

# Initialize app and create database tables
app = FastAPI(title="Clients API")

# Include routes
app.include_router(clients.router)
