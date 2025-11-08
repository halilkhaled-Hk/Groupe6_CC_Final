from fastapi import APIRouter, HTTPException
from models import Project
import json
import os


router = APIRouter(prefix="/projects", tags=["Projects"])


DB_PATH = "db.json"


def read_db():
    if not os.path.exists(DB_PATH):
        return []
    with open(DB_PATH, "r") as f:
        return json.load(f)


def write_db(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=4)


@router.post("/")
def add_project(project: Project):
    db = read_db()

    # Vérifier si l'URL GitHub existe déjà (optionnel)
    if any(p["githubUrl"] == project.githubUrl for p in db):
        raise HTTPException(status_code=400, detail="Ce projet existe déjà.")

    project.id = len(db) + 1
    db.append(project.dict())
    write_db(db)
    return {"message": "Projet ajouté avec succès", "project": project}
