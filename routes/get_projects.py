from fastapi import APIRouter, HTTPException
import json

router = APIRouter()

DB_PATH = "db.json"

@router.get("/projects")
def get_all_projects():
    try:
        with open(DB_PATH, "r") as f:
            data = json.load(f)
         data
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Fichier db.json introuvable")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))