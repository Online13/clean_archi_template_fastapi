from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel, func

class TimestampedModel(SQLModel):
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column_kwargs={
            "server_default": func.now(),
            "nullable": True,
        },
    )
    updated_at: datetime = Field(
        nullable=False,
        default=func.now(),
        sa_column_kwargs={"onupdate": func.now(), "server_default": func.now()},
    )

class BaseSQLModel(TimestampedModel):
    id: int | None = Field(primary_key=True, index=True, default=None)