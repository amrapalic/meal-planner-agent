# history_utils.py
import json
import os
from datetime import datetime

HISTORY_FILE = "meal_plan_history.json"


def save_meal_to_history(profile, feedback, meal_plan_text):
    history = load_history()

    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "profile": profile,
        "feedback": feedback,
        "meal_plan_text": meal_plan_text
    }

    history.append(entry)

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)


def get_recent_meal_plans():
    """
    Return a simplified version of each history entry for display.
    """
    history = load_history()
    return [
        {
            "timestamp": entry.get("date", "Unknown"),
            "name": entry["profile"].get("name", "User"),
            "meal_plan": entry.get("meal_plan_text", "No content available")
        }
        for entry in history
    ]
