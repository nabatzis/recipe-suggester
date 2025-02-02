from typing import Any, Dict
from app.models.models import RecipeRequest, RecipeResponse
from openai import OpenAI

from app.core.config import OPENAI_API_KEY
from app import logger

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_recipe(request: RecipeRequest) -> Dict[str, Any]:

    logger.debug("Prompt received: %s", request.content)

    prompt = f"Content for recipe:\n{request.content}\n"
    if request.context:
        prompt += f"\nAdditional context:\n{request.context}\n"

    if request.examples:
        prompt += "\nReference examples:\n"
        for i, example in enumerate(request.examples, 1):
            prompt += f"\nExample {i}:\n{example}\n"

    response = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[
        {"role": "system", "content": "You are a helpful assistant for meal preparation and knowledgable about ingredients and their calories."},
        {"role": "user", "content": prompt}
    ])
    
    recipe = response.choices[0].message.content

    return RecipeResponse(
        recipe=recipe,
        metadata={
            "status": "success",
            "model": "gpt-4-0125-preview"
        }
    )