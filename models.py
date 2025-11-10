from pydantic import BaseModel, HttpUrl
from typing import Optional


class Project(BaseModel):
    id: Optional[int] = None
    studentName: str
    course: str
    githubUrl: HttpUrl
    grade: Optional[float] = None
