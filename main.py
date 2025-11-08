from fastapi import FastAPI
from routes import post_project

app = FastAPI(title="ProjetAPI - TP GitHub DevOps")

# Inclusion des routes
app.include_router(post_project.router)


@app.get("/")
def root():
    return {"message": "Bienvenue sur ProjetAPI - FastAPI"}


@app.get("/lint-test")
def lint_test():
    # 👇 On garde le message d'erreur volontaire, mais indentation correcte
    return {
        "message": "Erreur d'indentation volontaire pour test de CI et LLM"
    }
