# routes/get_projects_by_course.py
from fastapi import APIRouter, HTTPException
from typing import List
import json
from models import Project

router = APIRouter(
    prefix="/projects",
    tags=["projects"]
)
DB_PATH = "db.json"

def read_db() -> List[Project]:
    try:
        with open(DB_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            raw_projects = data.get("projects", [])
            return [Project(**p) for p in raw_projects]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

@router.get("/course/{course_name}")
def get_projects_by_course(course_name: str | None = None):
    if course_name is None or not course_name.strip():
        raise HTTPException(
            status_code=400,
            detail="Le nom du cours est obligatoire"
        )

    projects = read_db()
    filtered = [
        p for p in projects
        if p.course.lower() == course_name.lower()
    ]


    if len(filtered) == 0:
        message = f"Aucun projet trouvé pour le cours \"{course_name}\""
    elif len(filtered) == 1:
        message = f"1 projet trouvé pour le cours \"{course_name}\""
    else:
        message = f"{len(filtered)} projets trouvés pour le cours \"{course_name}\""

    return {
        "success": True,
        "data": [p.model_dump() for p in filtered],
        "message": message
    }