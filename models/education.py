from __future__ import annotations

from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field


class EducationBase(BaseModel):
    person_id: UUID = Field(
        ...,
        description="ID of the person associated with this education record.",
        json_schema_extra={"example": "22222222-2222-4222-8222-222222222222"},
    )
    institution: str = Field(
        ...,
        description="Name of the educational institution.",
        json_schema_extra={"example": "Columbia University"},
    )
    degree: str = Field(
        ...,
        description="Degree or program pursued.",
        json_schema_extra={"example": "B.A. in Computer Science"},
    )
    start_year: int = Field(
        ...,
        description="Year studies began.",
        json_schema_extra={"example": 2022},
    )
    end_year: Optional[int] = Field(
        None,
        description="Year studies ended (if applicable).",
        json_schema_extra={"example": 2026},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "person_id": "22222222-2222-4222-8222-222222222222",
                    "institution": "Columbia University",
                    "degree": "B.A. in Computer Science",
                    "start_year": 2022,
                    "end_year": 2026,
                }
            ]
        }
    }


class EducationCreate(EducationBase):
    """Creation payload for an Education."""
    model_config = EducationBase.model_config


class EducationUpdate(BaseModel):
    """Partial update for an Education; supply only fields to change."""
    person_id: Optional[UUID] = None
    institution: Optional[str] = None
    degree: Optional[str] = None
    start_year: Optional[int] = None
    end_year: Optional[int] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"end_year": 2026},
                {"degree": "M.S. in Computer Science"},
            ]
        }
    }


class EducationRead(EducationBase):
    """Server representation returned to clients."""
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb",
                    "person_id": "22222222-2222-4222-8222-222222222222",
                    "institution": "Columbia University",
                    "degree": "B.A. in Computer Science",
                    "start_year": 2022,
                    "end_year": 2026,
                    "created_at": "2025-05-10T12:00:00Z",
                    "updated_at": "2025-05-15T15:30:00Z",
                }
            ]
        }
    }