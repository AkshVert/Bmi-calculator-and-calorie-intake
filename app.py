import pandas as pd

# Collect user data
age = int(input('Enter your age: '))
weight = float(input('Enter your weight in kg: '))
height = float(input('Enter your height in cm: '))
gender = input('Enter your gender (M/F): ')
fitness_goal = input('Enter your fitness goal (weight loss/muscle gain): ')

# Calculate user's BMI, BMR, and recommended daily calorie intake
bmi = weight / ((height / 100) ** 2)
if gender == 'M':
    bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
else:
    bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)
if fitness_goal == 'weight loss':
    calorie_intake = bmr * 0.8
else:
    calorie_intake = bmr * 1.2

# Classify user based on their BMI
if bmi < 18.5:
    bmi_category = 'underweight'
elif bmi < 25:
    bmi_category = 'normal'
elif bmi < 30:
    bmi_category = 'overweight'
else:
    bmi_category = 'obese'

# Create features that represent the user's physical characteristics and fitness goals
user_features = pd.DataFrame({
    'age': [age],
    'weight': [weight],
    'height': [height],
    'gender': ['M' if gender == 'M' else 'F'],
    'fitness_goal': ['weight loss' if fitness_goal == 'weight loss' else 'muscle gain' ],
    'bmi': [bmi],
    'bmi_category': [bmi_category],
    'bmr': [bmr],
    'calorie_intake': [calorie_intake]
})

# Print the user's features and recommended daily calorie intake
print(user_features)
print("As per your bmi, Your calorie_intake should be ",calorie_intake)

# Print a statement about the user's BMI category
print("You are classified as", bmi_category)
