from __future__ import annotations

from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime, date
from pydantic import BaseModel, Field


class EmploymentBase(BaseModel):
    person_id: UUID = Field(
        ...,
        description="ID of the person associated with this employment record.",
        json_schema_extra={"example": "11111111-1111-4111-8111-111111111111"},
    )
    organization: str = Field(
        ...,
        description="Name of the employing organization.",
        json_schema_extra={"example": "Amazon"},
    )
    position: str = Field(
        ...,
        description="Job title or role held.",
        json_schema_extra={"example": "Software Engineering Intern"},
    )
    start_date: date = Field(
        ...,
        description="Employment start date.",
        json_schema_extra={"example": "2025-05-01"},
    )
    end_date: Optional[date] = Field(
        None,
        description="Employment end date (if applicable).",
        json_schema_extra={"example": "2025-08-31"},
    )
    is_current: bool = Field(
        default=False,
        description="Whether this is the person's current job.",
        json_schema_extra={"example": True},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "person_id": "11111111-1111-4111-8111-111111111111",
                    "organization": "Amazon",
                    "position": "Software Engineering Intern",
                    "start_date": "2025-05-01",
                    "end_date": "2025-08-31",
                    "is_current": False,
                }
            ]
        }
    }


class EmploymentCreate(EmploymentBase):
    """Creation payload for an Employment."""
    model_config = EmploymentBase.model_config



class EmploymentUpdate(BaseModel):
    """Partial update for an Employment; supply only fields to change."""
    person_id: Optional[UUID] = None
    organization: Optional[str] = None
    position: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    is_current: Optional[bool] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"end_date": "2025-08-31", "is_current": False},
                {"position": "Software Engineer", "is_current": True},
            ]
        }
    }


class EmploymentRead(EmploymentBase):
    """Server representation returned to clients."""
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa",
                    "person_id": "11111111-1111-4111-8111-111111111111",
                    "organization": "Amazon",
                    "position": "Software Engineering Intern",
                    "start_date": "2025-05-01",
                    "end_date": "2025-08-31",
                    "is_current": False,
                    "created_at": "2025-05-10T12:00:00Z",
                    "updated_at": "2025-05-15T15:30:00Z",
                }
            ]
        }
    }