import random

# Greeting asking the user if they want PowerBall numbers
print("Welcome to the Powerball Generator!")
answer = input("Would you like some PowerBall numbers? (yes/no): ")

# If user wants PowerBall numbers
if answer.lower() == "yes":
    # Generate PowerBall numbers
    powerball_numbers = [random.randint(1, 69) for _ in range(5)]  # First 5 numbers
    powerball_numbers.append(random.randint(1, 26))  # PowerBall number
    
    # Convert numbers to string and format
    powerball_numbers_str = "  ".join(str(num) for num in powerball_numbers[:5]) + "    " + str(powerball_numbers[5])
    
    # Output the PowerBall numbers
    print("\nHere are your PowerBall numbers:")
    print(powerball_numbers_str)
else:
    print("No problem, maybe next time!")

# Farewell message
print("\nThank you for playing! Goodbye!")
