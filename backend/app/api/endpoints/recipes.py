from app.models.models import RecipeRequest, RecipeResponse
from fastapi import APIRouter, HTTPException

from app import logger
from app.services.openai_service import generate_recipe

router = APIRouter()

@router.post("/recipes/suggestions/", response_model=RecipeResponse)
def get_recipe_suggestions(request: RecipeRequest):
    try:
        logger.info("Input: %s", request.content)
        suggestions = generate_recipe(request)
        return suggestions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))