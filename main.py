from fastapi import FastAPI
from routes import post_project
from routes import get_projects
from routes import get_project_by_id

app = FastAPI(title="ProjetAPI - TP GitHub DevOps")

# Inclusion des routes
app.include_router(post_project.router)
app.include_router(get_projects.router)
app.include_router(get_project_by_id.router)


@app.get("/")
def root():
    return {"message": "Bienvenue sur ProjetAPI - FastAPI"}


@app.get("/lint-test")
def lint_test():
    return {
        "message": "Erreurs d'indentation volontaire pour test de CI et LLM"
    }  # 👈 indentation volontairement incorrecte (3 espaces)
