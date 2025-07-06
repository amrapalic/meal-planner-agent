import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama2"  # Change to your actual model name if different

# ----- Meal Plan Generation -----

def get_meal_plan_from_llm(profile):
    prompt = generate_meal_plan_prompt(profile)

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


def generate_meal_plan_prompt(profile):
    return f"""
You are a smart meal planning assistant.

Create a personalized meal plan for a user based on the following profile:

- Name: {profile.get('name')}
- Age: {profile.get('age')}
- Gender: {profile.get('gender')}
- Weight: {profile.get('weight')} kg
- Height: {profile.get('height')} cm
- Activity Level: {profile.get('activity_level')}
- Fitness Goal: {profile.get('goal')}
- Diet Type: {profile.get('diet_type')}
- Macro Preference or Style: {profile.get('macro_style')}

Please generate a meal plan that includes the following:
- Meals: Breakfast, Mid-Morning Snack, Lunch, Evening Snack, and Dinner
- Recipes with names, ingredients, and basic cooking instructions
- Macronutrient breakdown for each meal (calories, protein, carbs, fiber, fat)
- Format the output in clean, well-structured Markdown. No extra fluff or greetings.

Example format:
## Breakfast
- Name: Greek Yogurt with Berries and Nuts
- Ingredients: Greek yogurt, mixed berries, almonds
- Instructions: Mix all ingredients in a bowl and enjoy.
- **Macros**: 300 kcal, 25g protein, 15g carbs, 5g fiber, 10g fat
""".strip()


# ----- Single Recipe Generator -----

def get_recipe_from_ingredients(ingredients, preferences=""):
    prompt = f"""
You are a helpful and concise recipe assistant.

Given the following ingredients:

{ingredients}

{f"And preferences: {preferences}" if preferences else ""}

Please return only the following sections in markdown:

### Recipe Name

### Ingredients
- List ingredients

### Instructions
1. Step-by-step cooking instructions

### Nutritional Information (approximate)
- Calories
- Protein
- Carbs
- Fats
- Fiber

Do NOT include greetings or conversational phrases. Just output the recipe directly using clean markdown.
""".strip()

    response = requests.post(
        OLLAMA_URL,
        json={"model": MODEL_NAME, "prompt": prompt, "stream": False}
    )
    response.raise_for_status()
    return response.json()['response'].strip()
