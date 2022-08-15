from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional


def generate_uuid():
    return UUID(str(uuid4()))


class StudentSchema(BaseModel):
    """Represents a student model for the student API."""

    id: Optional[UUID]
    name: str
    department: str
    year: int
