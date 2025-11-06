import logging
from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session
from . import models, database
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

# 🧩 Configuration des logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
)
logger = logging.getLogger("notes-backend")

# 🧱 DB init
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Notes API - FastAPI")

# 🌍 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔌 DB Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🧠 Middleware pour tracer chaque requête
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = datetime.now()
    logger.info(f"➡️ Requête {request.method} {request.url}")
    response = await call_next(request)
    process_time = (datetime.now() - start_time).total_seconds()
    logger.info(f"⬅️ Réponse {response.status_code} ({process_time:.2f}s)")
    return response

@app.get("/api/health")
def health_check():
    logger.info("✅ Vérification de santé OK")
    return {"status": "ok"}

@app.get("/api/notes")
def get_notes(db: Session = Depends(get_db)):
    logger.info("📥 Lecture des notes depuis la base")
    try:
        notes = db.query(models.Note).all()
        logger.info(f"✅ {len(notes)} notes trouvées")
        return notes
    except Exception as e:
        logger.exception("❌ Erreur lors de la récupération des notes")
        return {"error": str(e)}

@app.post("/api/notes")
def create_note(note: dict, db: Session = Depends(get_db)):
    logger.info(f"📝 Création d'une note : {note}")
    try:
        new_note = models.Note(title=note["title"], content=note["content"])
        db.add(new_note)
        db.commit()
        db.refresh(new_note)
        logger.info(f"✅ Note créée avec ID {new_note.id}")
        return new_note
    except Exception as e:
        logger.exception("❌ Erreur lors de la création d'une note")
        return {"error": str(e)}
