def get_age_input():
    while True:
        try:
            # Prompt the user for age input
            age = int(input("Please enter your age: "))

            # Check if the age is a valid positive number
            if age < 0:
                print("Invalid input. Age cannot be negative. Try again.")
            else:
                return age
        except ValueError:
            # Handle non-numeric input
            print("Invalid input. Please enter a valid number for age.")


def classify_age(age):
    # Classify the person's age
    if age < 18:
        return "Minor"
    elif 18 <= age <= 65:
        return "Adult"
    else:
        return "Senior Citizen"


age = get_age_input()  # Get valid age input from the user
category = classify_age(age)  # Classify the age


print(f"Based on your age, you are classified as: {category}")
