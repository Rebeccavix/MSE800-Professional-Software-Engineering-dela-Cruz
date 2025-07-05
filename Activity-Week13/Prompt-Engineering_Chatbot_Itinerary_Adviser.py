import os
from together import Together

# Set your API key
API_KEY = "ab69bda264a79a50998f18d05d1b1626558e42be423a7e46331039739de9c3f8"
client = Together(api_key=API_KEY)


def instructor_chatbot():
    """Command-line AI Itinerary Chatbot."""
    print("Welcome to AI Itinerary recommender! Answer a few questions to get personalized itinerary advice.\n")

    days = input("How many days will you stay? ")
    location = input("What is your destination (city name)? ")
    age = input("Enter your age: ")

    # Construct prompt
    prompt = f"""
    You are a professional tourist recommender. Provide an itinerary recommendation based on user data.

    User Details:
    - Days: {days}
    - Destination: {location}
    - Age: {age}

    Based on this information, give a structured itinerary with the name of the place, address, and a short description for each day, with a maximum of three activities per day.
    """

    try:
        # Call the Together API with the Llama model
        response = client.chat.completions.create(
            model="meta-llama/Llama-Vision-Free",
            messages=[
                {"role": "system",
                    "content": "You are a professional itinerary recommender."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )

        print("\nMy name is Hadi, your AI Itinerary expert:")
        # Access the content correctly
        for choice in response.choices:
            print(choice.message.content)

    except Exception as e:
        print("Error communicating with Together API:", e)


# Run the chatbot
if __name__ == "__main__":
    instructor_chatbot()
