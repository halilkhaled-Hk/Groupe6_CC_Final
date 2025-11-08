from fastapi import FastAPI
from routes import post_project, get_project_by_id

app = FastAPI(title="ProjetAPI - TP GitHub DevOps")

# Inclusion des routes
app.include_router(post_project.router)
app.include_router(get_project_by_id.router)

@app.get("/")
def root():
    return {"message": "Bienvenue sur ProjetAPI - FastAPI"}
