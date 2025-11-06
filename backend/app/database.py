import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

logger = logging.getLogger("database")

DATABASE_URL = os.getenv("DATABASE_URL")

logger.info(f"🔗 Connexion à la base de données : {DATABASE_URL}")

engine = create_engine(DATABASE_URL, echo=True)  # echo=True => log SQL
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
