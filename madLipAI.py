# Instructions for the user
print("Welcome to the Mad Lib game!")
print("Please provide the following words when prompted:")

# Ask the user for input
large_object = input("Enter a large object: ")
large_objects_plural = input("Enter large objects (plural): ")
adjective = input("Enter an adjective: ")
body_part = input("Enter a body part: ")
restaurant = input("Enter a restaurant: ")
food1 = input("Enter a food: ")
food2 = input("Enter another food: ")

# Fill in the Mad Lib with user input
mad_lib_story = f"I’ve had a very {adjective} day. This morning, I dropped a box of {large_objects_plural} on my {body_part}. Then, at lunch, I went to {restaurant} for their delicious {food1}, But the waiter brought me {food2}, which I was not hungry for. Finally, on my way home, I was cut off by a van with a large {large_object} strapped to the roof."

# Print the completed Mad Lib
print("\nHere's your Mad Lib:\n")
print(mad_lib_story)