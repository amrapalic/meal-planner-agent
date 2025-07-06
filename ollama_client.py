import requests
from prompts.meal_plan_prompt import meal_plan_prompt_template
from prompts.recipe_from_ingredients_prompt import recipe_prompt_template

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama2"  # Change to your actual model name if different

# ----- Meal Plan Generation -----

def get_meal_plan_from_llm(profile):
    prompt = meal_plan_prompt_template.format(
        name=profile.get("name"),
        age=profile.get("age"),
        gender=profile.get("gender"),
        weight=profile.get("weight"),
        height=profile.get("height"),
        activity_level=profile.get("activity_level"),
        goal=profile.get("goal"),
        diet_type=profile.get("diet_type"),
        macro_style=profile.get("macro_style")
    )

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "No response received from the model.")
    except Exception as e:
        return f"Error during LLM call: {e}"


# ----- Single Recipe Generator -----

def get_recipe_from_ingredients(ingredients, preferences=""):
    preferences_text = f"And preferences: {preferences}" if preferences else ""
    prompt = recipe_prompt_template.format(
        ingredients=ingredients,
        preferences=preferences_text
    )

    response = requests.post(
        OLLAMA_URL,
        json={"model": MODEL_NAME, "prompt": prompt, "stream": False}
    )
    response.raise_for_status()
    return response.json()['response'].strip()
