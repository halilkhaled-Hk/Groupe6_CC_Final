from fastapi import APIRouter, HTTPException
import json

router = APIRouter()

DB_PATH = "db.json"

@router.get("/projects/{id}")
def get_project_by_id(id: int):
    try:
        with open(DB_PATH, "r") as f:
            data = json.load(f)
        project = next((p for p in data if p["id"] == id), None)
        if not project:
            raise HTTPException(status_code=404, detail="Projet introuvable")
        return project
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Fichier db.json introuvable")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
