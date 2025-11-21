from fastapi import FastAPI, Depends, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from .database import engine, Base, get_db
from .models import Note
from .config import settings

# Créer les tables
Base.metadata.create_all(bind=engine)

# Application FastAPI
app = FastAPI(title="Notes API Simple")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Schémas Pydantic
class NoteCreate(BaseModel):
    title: str
    content: str = ""


class NoteResponse(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True


# Vérification du token
def verify_token(x_api_token: str = Header(None)):
    """Vérifie que le token API est correct"""
    if x_api_token != settings.API_TOKEN:
        raise HTTPException(status_code=401, detail=f"Token invalide. Reçu: {x_api_token}, Attendu: {settings.API_TOKEN}")
    return x_api_token


# Routes
@app.get("/")
def root():
    """Route de base"""
    return {"message": "Notes API Simple - Utilisez /notes avec le header X-API-Token"}


@app.get("/notes", response_model=List[NoteResponse])
def get_notes(
    db: Session = Depends(get_db),
    token: str = Depends(verify_token)
):
    """Récupérer toutes les notes (nécessite token)"""
    notes = db.query(Note).all()
    return notes


@app.post("/notes", response_model=NoteResponse)
def create_note(
    note: NoteCreate,
    db: Session = Depends(get_db),
    token: str = Depends(verify_token)
):
    """Créer une nouvelle note (nécessite token)"""
    db_note = Note(title=note.title, content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note
