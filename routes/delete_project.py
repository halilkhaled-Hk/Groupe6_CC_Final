from fastapi import APIRouter, HTTPException
import json
import os

router = APIRouter()

DB_PATH = "db.json"


@router.delete("/projects/{id}")
def delete_project(id: int):
    if not os.path.exists(DB_PATH):
        raise HTTPException(
            status_code=404, detail="Projet introuvable dans la base de données."
        )

    try:
        # Charger les projets existants
        with open(DB_PATH, "r") as f:
            data = json.load(f)

        # Trouver le projet à supprimer
        project = next((p for p in data if p["id"] == id), None)

        if not project:
            raise HTTPException(status_code=404, detail="Projet introuvable")

        # Supprimer le projet
        data = [p for p in data if p["id"] != id]

        # Réécrire le fichier
        with open(DB_PATH, "w") as f:
            json.dump(data, f, indent=4)

        # Ligne corrigée pour Flake8 (moins de 79 caractères)
        return {"message": f"Projet avec id {id} supprimé avec succès."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
