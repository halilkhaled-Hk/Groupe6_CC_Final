from fastapi import APIRouter, HTTPException
import json

router = APIRouter()

DB_PATH = "db.json"


@router.put("/projects/{project_id}/grade")
def put_projects_id_grade(project_id: int, grade: int):

    # Charger la DB
    try:
        with open(DB_PATH, "r") as f:
            projects = json.load(f)  # ✅ Ici c'est une LISTE, pas un dict
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Database file not found")

    # Parcourir la liste
    for project in projects:
        if project["id"] == project_id:

            # Mettre à jour la note
            project["grade"] = grade

            # Écrire la liste mise à jour dans db.json
            with open(DB_PATH, "w") as f:
                json.dump(projects, f, indent=4)

            return {"message": (f"note projet {project_id} " f"enregistrée")}

    # Si le projet n’est pas trouvé
    raise HTTPException(status_code=404, detail="Project not found")
