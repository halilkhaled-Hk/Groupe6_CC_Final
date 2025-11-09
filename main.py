from fastapi import FastAPI
from routes import post_project
from routes import get_projects
from routes import get_project_by_id
import sys,os  # E401: multiple imports on one line (Flake8)

app = FastAPI(title="ProjetAPI - TP GitHub DevOps")

# Inclusion des routes
app.include_router(post_project.router)
app.include_router(get_projects.router)
app.include_router(get_project_by_id.router)


@app.get("/")
def root():
    return {"message": "Bienvenue sur ProjetAPI REST- FastAPI"}


@app.get("/lint-test")
def lint_test():
    # E501: line too long (Flake8 - plus de 79 caractères)
    very_long_variable_name_that_exceeds_the_maximum_line_length = "Cette ligne est intentionnellement trop longue pour faire échouer Flake8"
    
    x=1+2+3  # E225: missing whitespace around operator (Flake8)
    
    unused_variable = "jamais utilisée"  # F841: local variable is assigned but never used (Flake8)
    
       return {  # E117: over-indented (3 espaces au lieu de 4)
        "message": "Erreurs d'indentation volontaire pour test de CI et LLM",
           "errors": [ "indentation", "line_length","spacing" ]  # E231: missing whitespace after ','
    }


@app.get( "/format-test" )  # Black va détecter les espaces inutiles
def format_test( ):  # Black va détecter les espaces inutiles dans les paramètres
    data={'key':'value','number':123}  # Black exige des espaces autour de : et après ,
    return data


# E302: expected 2 blank lines, found 1 (Flake8)
@app.get("/spacing-test")
def spacing_test():
    result={"status":"error"}  # E225 + Black formatage
    return result