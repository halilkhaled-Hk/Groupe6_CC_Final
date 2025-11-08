from fastapi import FastAPI
from routes import post_project
from routes import get_projects
app = FastAPI(title="ProjetAPI - TP GitHub DevOps")

# Inclusion des routes
app.include_router(post_project.router)
app.include_router(get_projects.router)

@app.get("/")
def root():
    return {"message": "Bienvenue sur ProjetAPI - FastAPI"}
