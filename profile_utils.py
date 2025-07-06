def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 2)

def calculate_bmr(weight_kg, height_cm, age, gender):
    if gender.lower() == "male":
        return round(10 * weight_kg + 6.25 * height_cm - 5 * age + 5, 2)
    else:
        return round(10 * weight_kg + 6.25 * height_cm - 5 * age - 161, 2)

def calculate_tdee(bmr, activity_level):
    activity_multipliers = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725
    }
    multiplier = activity_multipliers.get(activity_level, 1.2)
    return round(bmr * multiplier, 2)
