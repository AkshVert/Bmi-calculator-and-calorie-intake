# BMI Calculator and Calorie Intake Recommender

This program allows users to calculate their body mass index (BMI) and recommended daily calorie intake based on their physical characteristics and fitness goals. It also classifies users based on their BMI category.

## Requirements

This program requires the following packages to be installed:

- pandas

## Usage

To use this program, run the following command in your terminal:

```
python app.py
```

You will be prompted to enter your age, weight, height, gender, and fitness goal. The program will then calculate your BMI, BMR, and recommended daily calorie intake, and classify you based on your BMI category. The results will be displayed on the screen in a pandas DataFrame format.

## Example

Here's an example of what the program output might look like:

```
Enter your age: 25
Enter your weight in kg: 70
Enter your height in cm: 175
Enter your gender (M/F): M
Enter your fitness goal (weight loss/muscle gain): weight loss
    age   weight   height  gender  fitness_goal     bmi       bmi_category  
    25.0    70.0   175.0      M    weight loss    22.857143       normal   

          bmr  calorie_intake  
0  1641.40864      1313.12691  

As per your bmi, Your calorie_intake should be  1313.12690983376
You are classified as normal
```

## License

This program is licensed under the MIT License. See the LICENSE file for details.
