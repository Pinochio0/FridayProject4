# Define the dictionary of questions and answers
questions_dict = {
    "What is the capital of France?": "Paris",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the chemical symbol for water?": "H2O",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who painted the Mona Lisa?": "Leonardo da Vinci"
}

# Iterate over each question in the dictionary
for question, answer in questions_dict.items():
    # Display the question to the user
    print(question)
    
    # Prompt the user to input their answer
    user_answer = input("Your answer: ")
    
    # Check if the user's answer matches the correct answer
    if user_answer.lower() == answer.lower():
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", answer)
    
    # Ask the next question
    print()  # Add a blank line for better readability

print("End of questions.")
