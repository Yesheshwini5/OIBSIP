# OIBSIP
# BMI Calculator
# Beginner Tier
# Calculates BMI and classifies the result

def calculate_bmi():
    print("===== BMI CALCULATOR =====")

    # Get weight
    while True:
        try:
            weight = float(input("Enter your weight in kilograms (kg): "))

            if weight <= 0:
                print("Error: Weight must be greater than 0.")
                continue

            break

        except ValueError:
            print("Error: Please enter a valid numeric value for weight.")

    # Get height
    while True:
        try:
            height = float(input("Enter your height in meters (m): "))

            if height <= 0:
                print("Error: Height must be greater than 0.")
                continue

            break

        except ValueError:
            print("Error: Please enter a valid numeric value for height.")

    # Calculate BMI
    bmi = weight / (height ** 2)

    # Classify BMI
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    # Display result
    print("\n===== BMI RESULT =====")
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")


# Run the program
calculate_bmi()
