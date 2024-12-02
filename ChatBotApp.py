import openai
import os
from dotenv import load_dotenv
from apikey import apikey

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY") or apikey  # Use .env or fallback to apikey.py

# Function to generate response from OpenAI API
def generate_response(user_input):
    try:
        # Define the message history (including system, assistant, and user)
        messages = [
            {"role": "system", "content": "You are a wonderful assistant for aspiring chefs named Bella, and you help them find delicious recipes, suggest creative meal ideas, and guide them through cooking step-by-step. You are knowledgeable about various cuisines, dietary restrictions, and cooking techniques. Your goal is to make cooking enjoyable and accessible for everyone."},
            {"role": "assistant", "content": "Hello fellow chef! What is your name?"},
            {"role": "user", "content": "Hello. My name is Jack."},
            {"role": "user", "content": "Tell me a recipe."},
            {"role": "assistant", "content": "To make a quick and delicious garlic butter pasta, start by cooking 200g of spaghetti in salted boiling water according to the package instructions. Once cooked, drain the pasta and set it aside. In a large pan, melt 3 tablespoons of butter over medium heat, then add 3 minced garlic cloves and sauté them until fragrant, which should take about 1-2 minutes. Add the cooked spaghetti to the pan and toss it well to coat the noodles in the garlic butter. Season with salt and pepper to taste. For an extra touch, garnish with grated Parmesan cheese and freshly chopped parsley before serving. Enjoy your simple and flavorful meal! 🍝"},
            {"role": "user", "content": "Tell me more recipes."},
            {"role": "assistant", "content": "For a quick and tasty turkey stir-fry, start by slicing 200g of turkey breast into thin strips. Heat a tablespoon of olive oil in a large pan or wok over medium-high heat. Add the turkey strips and cook for about 5-7 minutes until browned and cooked through. Remove the turkey from the pan and set aside. In the same pan, add a bit more oil if needed, and sauté a chopped onion, 1 bell pepper, and 2 cloves of garlic for about 3-4 minutes, until softened. Then, add 2 tablespoons of soy sauce, 1 tablespoon of honey, and a pinch of black pepper to the vegetables, stirring to combine. Return the turkey to the pan, toss everything together, and cook for an additional 2 minutes until everything is well-coated and heated through. Serve your turkey stir-fry over rice or noodles, and enjoy a flavorful, healthy meal!"},
            {"role": "assistant", "content": "Quick Chicken Stir-Fry Ingredients: Chicken breast, bell pepper, soy sauce, garlic, olive oil. Instructions: Slice chicken and bell pepper. Sauté garlic in olive oil, add chicken and cook until browned. Add bell pepper and soy sauce, stir-fry for 5 minutes. Serve over rice."},
            {"role": "assistant", "content": "Simple Veggie Salad Ingredients: Lettuce, cherry tomatoes, cucumber, olive oil, lemon, salt. Instructions: Chop lettuce, tomatoes, and cucumber. Toss with olive oil, lemon juice, and a pinch of salt. Serve :)"},
            {"role": "user", "content": "What was your first recipe?"},
            {"role": "user", "content": "What was your second recipe?"},
            {"role": "user", "content": "What was your third recipe?"},
            {"role": "user", "content": "What was your fourth recipe?"}
        ]  # This list simulates the conversation history

        # Add the latest user input to the message history
        messages.append({"role": "user", "content": user_input})

        # Make the API call to OpenAI
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Extract and return the chatbot's response
        response_text = completion.choices[0].message['content']
        return response_text

    except Exception as e:
        # Handle errors and return an error message
        print(f"Error generating response: {e}")
        return "I'm sorry, I couldn't generate a response."

# Main function to interact with the user
def main():
    # Print a welcome message
    print("\nWelcome to the Recipe Suggester Chatbot! Type 'quit' to exit.\n")

    # This loop will run until the user types "quit"
    while True:
        # Get user input
        user_input = input("Aspiring Chef Question: ")

        # Check if user wants to quit the chatbot
        if user_input.lower() == "quit":
            print("Exiting Recipe Suggester Bot.")
            break

        # Generate a response using OpenAI's GPT-3.5-turbo
        response = generate_response(user_input)

        # Print the response
        print(f"Recipe Suggester Bot: {response}")

# Run the main function
if __name__ == "__main__":
    main()