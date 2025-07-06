from langchain.prompts import PromptTemplate

recipe_prompt_template = PromptTemplate(
    input_variables=["ingredients", "preferences"],
    template="""
You are a helpful and concise recipe assistant.

Given the following ingredients:

{ingredients}

{preferences}

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
)
