def calculate_bmi(weight, height):
    """Calculate BMI using the formula: weight (kg) / (height (m) ** 2)"""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classify BMI into categories"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def get_user_input():
    """Get user input for weight and height with validation"""
    while True:
        try:
            weight = float(input("Enter your weight in kilograms: "))
            height = float(input("Enter your height in meters: "))
            if weight <= 0 or height <= 0:
                print("Weight and height must be positive numbers. Please try again.")
                continue
            return weight, height
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def main():
    print("Welcome to the BMI Calculator!")
    weight, height = get_user_input()
    
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)
    
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")

if __name__ == "__main__":
    main()
