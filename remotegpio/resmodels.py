"""
These models represent the expected input and output formats of the HTTP API
using Pydantic.
"""
from __future__ import annotations
from typing import List, Optional, NamedTuple

from pydantic import BaseModel, Extra, validator
from pydantic.fields import ModelField


def not_empty(v: Optional[str], field: ModelField) -> Optional[str]:
    if v is not None and len(v) == 0:
        raise ValueError(f'"{field.name}" field cannot be empty')
    return v
