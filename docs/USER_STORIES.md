# 📋 User Stories – AI Meal Planner Project

This document outlines the complete set of user stories that were implemented to build the AI Meal Planner app.

---

| **Description**             | **User Story**                                                                                                                                        | **Status** |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| Developer Environment Setup | As a developer, I want to set up Ollama on my machine, so that I can run a local LLM instance for testing and development.                            | ✅ Done     |
|                             | As a developer, I want to configure a Python virtual environment, so that I can manage project dependencies in isolation.                             | ✅ Done     |
|                             | As a developer, I want to install all required dependencies from `requirements.txt`, so that the app runs with all needed packages.                   | ✅ Done     |
|                             | As a developer, I want to run a basic test LLM prompt, so that I can verify that the Ollama and model integration works.                              | ✅ Done     |
|                             | As a developer, I want to integrate LangChain into the project, so that I can use structured output parsing and prompt templates easily.              | 🕒 Planned |
| Recipe Generator            | As a user, I want to input a list of ingredients, so that I can receive a simple and healthy recipe suggestion.                                       | ✅ Done     |
|                             | As a user, I want the recipe output to be clean and free of conversational filler, so that it's easy to read and follow.                              | ✅ Done     |
| Profile Setup               | As a user, I want to enter my profile details (name, age, gender, height, weight, activity level, etc.), so that the meal plan can be tailored to me. | ✅ Done     |
|                             | As a user, I want to see a summary of my profile on the sidebar, so that I can verify the data used for meal planning.                                | ✅ Done     |
|                             | As a user, I want the app to calculate my BMI, so that I can understand my body composition.                                                          | ✅ Done     |
|                             | As a user, I want the app to calculate my BMR and TDEE, so that I understand my daily calorie needs based on activity level.                          | ✅ Done     |
| Meal Plan Generation        | As a user, I want the AI to generate a full day meal plan based on my profile, so that I can follow a personalized nutrition routine.                 | ✅ Done     |
|                             | As a user, I want to see clearly formatted sections (Breakfast, Lunch, etc.), so that I can easily navigate the meal plan.                            | ✅ Done     |
|                             | As a user, I want macronutrient breakdowns for each meal, so that I can track calories, protein, carbs, fiber, and fat.                               | ✅ Done     |
|                             | As a user, I want the ability to regenerate a meal plan if I don’t like it, so that I can find something better suited to my preferences.             | 🕒 Planned |
| Meal Plan History           | As a user, I want each generated meal plan to be stored locally, so that I can revisit previous meal plans.                                           | ✅ Done     |
|                             | As a user, I want to see a tab called "Meal History" with a timeline view, so that I can browse past plans easily by date.                            | ✅ Done     |
| PDF Export                  | As a user, I want to export my recipe as a PDF, so that I can print or save it for offline access.                                                    | 🕒 Planned |
|                             | As a user, I want to see a grocery list in the PDF that separates what I have from what I need, so that I can shop efficiently.                       | 🕒 Planned |
| Automated Daily Meal Plans  | As a user, I want the app to automatically generate and send my meal plan daily (via email), so that I never miss my nutrition routine.               | 🕒 Planned |
| LangChain Integration       | As a developer, I want to use PromptTemplate and LLMChain with Ollama, so that prompt creation and chaining becomes easier.                           | 🕒 Planned |
|                             | As a developer, I want to define structured output using Pydantic models and parse responses, so that I can reliably extract recipe and meal data.    | 🕒 Planned |
