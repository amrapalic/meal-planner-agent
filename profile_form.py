import streamlit as st
import time

def show_profile_form():
    st.title("Let's Get to Know You")
    st.write("Before we can generate personalized meals for you, we need to know a bit about your lifestyle and preferences.")

    # Default values
    default_name = "Amy"
    default_age = 29
    default_gender = "Female"
    default_weight = 80.0
    default_height = 169.0
    default_activity_label = "Moderately Active (3–5 days/week)"
    default_goal = "Lose Weight"
    default_diet_type = "Omnivore"
    default_diet_style = "Balanced"

    # Activity levels with explanation
    activity_levels = {
        "Sedentary (Little to no exercise)": "Sedentary",
        "Lightly Active (1–2 days/week)": "Lightly Active",
        "Moderately Active (3–5 days/week)": "Moderately Active",
        "Very Active (6–7 days/week)": "Very Active"
    }

    activity_display_options = list(activity_levels.keys())
    default_activity_index = activity_display_options.index(default_activity_label)

    # Form inputs
    name = st.text_input("Name", value=default_name)
    age = st.number_input("Age", min_value=10, max_value=100, value=default_age)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"], index=1)
    weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=default_weight)
    height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=default_height)
    activity_display = st.selectbox("Activity Level", activity_display_options, index=default_activity_index)
    activity_level = activity_levels[activity_display]  # internal value
    goal = st.selectbox("Fitness Goal", ["Lose Weight", "Maintain Weight", "Gain Muscle"], index=0)
    diet_type = st.selectbox(
        "Diet Type",
        ["Omnivore", "Vegetarian", "Vegan", "Pescetarian", "Flexitarian", "Other"],
        index=0
    )
    diet_style = st.selectbox(
        "Macro Preference / Diet Style",
        ["Balanced", "Low-Carb", "High-Protein", "Low-Fat", "Keto", "Paleo", "Mediterranean", "Other"],
        index=0
    )

    # Submit button
    if st.button("Next"):
        with st.spinner("Saving your profile..."):
            profile = {
                "name": name,
                "age": age,
                "gender": gender,
                "weight": weight,
                "height": height,
                "activity_level": activity_level,
                "goal": goal,
                "diet_type": diet_type,
                "diet_style": diet_style
            }
            st.session_state.profile = profile
            st.session_state.profile_submitted = True
            time.sleep(1)
        st.rerun()
