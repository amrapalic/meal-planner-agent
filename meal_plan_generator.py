# mealplan_generator.py

import requests
import json
import streamlit as st

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def build_prompt_from_profile(profile):
    prompt = f"""
You are a nutritionist and meal planner. Based on the following user profile, create a one-day meal plan including breakfast, mid-morning snack, lunch, evening snack, and dinner. Each meal should include a dish name, short description, ingredients, and macronutrient breakdown (calories, protein, carbs, fats, fiber).

User Profile:
- Name: {profile['name']}
- Age: {profile['age']}
- Gender: {profile['gender']}
- Weight: {profile['weight']} kg
- Height: {profile['height']} cm
- Activity Level: {profile['activity_level']}
- Fitness Goal: {profile['goal']}
- Diet Type: {profile['diet_type']}
- Macro Preference: {profile['macro_style']}

Output format (Markdown preferred):
1. Meal name
2. Description
3. Ingredients
4. Macronutrients (in a table)
Repeat for all 5 meals.
"""
    return prompt

def get_meal_plan(profile):
    prompt = build_prompt_from_profile(profile)
    response = requests.post(OLLAMA_API_URL, json={
        "model": "llama3",  # use your installed model name
        "prompt": prompt,
        "stream": False
    })

    result = response.json()
    return result.get("response", "No response from LLM.")
