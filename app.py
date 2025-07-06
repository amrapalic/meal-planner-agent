### app.py
import streamlit as st
from profile_form import show_profile_form
from profile_utils import calculate_bmi, calculate_bmr, calculate_tdee
from ollama_client import get_meal_plan_from_llm, get_recipe_from_ingredients
from history_utils import save_meal_to_history, load_history
import re

# Set page config
st.set_page_config(page_title="Daily AI Meal Planner", layout="wide")

# Initialize session state
if 'profile_submitted' not in st.session_state:
    st.session_state.profile_submitted = False
if 'profile' not in st.session_state:
    st.session_state.profile = {}
if 'meal_plan' not in st.session_state:
    st.session_state.meal_plan = None

# Show form if profile not submitted
if not st.session_state.profile_submitted:
    st.title("Welcome to the AI-Powered Meal Planner")
    st.markdown("Before we can generate personalized meals for you, we need to know a bit about you.")
    show_profile_form()
    st.stop()

# Profile submitted
profile = st.session_state.profile
bmi = calculate_bmi(profile['weight'], profile['height'])
bmr = calculate_bmr(profile['weight'], profile['height'], profile['age'], profile['gender'])
tdee = calculate_tdee(bmr, profile['activity_level'])

# Tabs
tab1, tab2, tab3 = st.tabs(["🍽️ Generate Meal Plan", "📜 Meal History", "🧪 Generate Recipe"])

# --- TAB 1: Generate Meal Plan --- #
with tab1:
    st.sidebar.header("Your Profile Summary")
    st.sidebar.markdown(f"**Name:** {profile.get('name', 'N/A')}")
    st.sidebar.markdown(f"**Age:** {profile.get('age', 'N/A')}")
    st.sidebar.markdown(f"**Gender:** {profile.get('gender', 'N/A')}")
    st.sidebar.markdown(f"**Weight:** {profile.get('weight', 'N/A')} kg")
    st.sidebar.markdown(f"**Height:** {profile.get('height', 'N/A')} cm")
    st.sidebar.markdown(f"**Activity Level:** {profile.get('activity_level', 'N/A')}")
    st.sidebar.markdown(f"**Fitness Goal:** {profile.get('goal', 'N/A')}")
    st.sidebar.markdown(f"**Diet Type:** {profile.get('diet_type', 'N/A')}")
    st.sidebar.markdown(f"**Macro Style:** {profile.get('macro_style', 'Not specified')}")

    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**BMI:** {bmi:.2f}")
    st.sidebar.markdown(f"**BMR:** {bmr:.0f} kcal/day")
    st.sidebar.markdown(f"**Estimated TDEE:** {tdee:.0f} kcal/day")

    st.title(f"Welcome back, {profile['name']}!")
    st.markdown("👈 You can find your profile and stats on the left. Let's get started on your meal plan next!")

    if st.button("Generate Meal Plan"):
        with st.spinner("Generating your personalized meal plan with AI..."):
            try:
                plan = get_meal_plan_from_llm(profile)
                st.session_state.meal_plan = plan
                save_meal_to_history(profile, "", plan)
            except Exception as e:
                st.error(f"Error generating meal plan: {e}")
                st.session_state.meal_plan = None

    if st.session_state.meal_plan:
        meal_plan_text = st.session_state.meal_plan
        sections = re.split(r"\*\*(.+?):\*\*", meal_plan_text)

        if len(sections) > 1:
            st.subheader("📅 Your AI-Generated Meal Plan")
            for i in range(1, len(sections), 2):
                meal_name = sections[i].strip()
                meal_content = sections[i + 1].strip()
                with st.expander(f"🍽️ {meal_name.capitalize()}"):
                    st.markdown(meal_content)
        else:
            st.markdown(meal_plan_text)

# --- TAB 2: Meal History --- #
with tab2:
    st.title("📜 Your Meal Plan History")
    history = load_history()

    if not history:
        st.info("No meal plans generated yet.")
    else:
        for entry in reversed(history):
            with st.expander(f"🗓️ {entry['date']}"):
                st.markdown("### Profile")
                st.json(entry['profile'])
                st.markdown("### Meal Plan")
                st.markdown(entry['meal_plan_text'])

# --- TAB 3: Generate Recipe --- #
with tab3:
    st.title("🧪 Generate a Recipe Based on Your Ingredients")

    ingredients = st.text_area("What ingredients do you have?", placeholder="e.g. lentils, tomatoes, garlic, spinach")
    preferences = st.text_input("Any preferences or dislikes?", placeholder="e.g. No dairy. Want something spicy.")

    if st.button("Generate Recipe"):
        if not ingredients.strip():
            st.warning("Please enter at least one ingredient.")
        else:
            with st.spinner("Cooking up a recipe with AI..."):
                try:
                    recipe = get_recipe_from_ingredients(ingredients, preferences)
                    st.markdown("### 🍳 Here's a recipe suggestion:")
                    st.markdown(recipe)
                except Exception as e:
                    st.error(f"Error generating recipe: {e}")
