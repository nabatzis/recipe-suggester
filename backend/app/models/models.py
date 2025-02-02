from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from enum import Enum


class RecipeRequest(BaseModel):
    content: str = Field(..., description="Code or content to document")
    context: Optional[Dict[str, Any]] = None
    examples: Optional[List[str]] = None

class RecipeResponse(BaseModel):
    recipe: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
