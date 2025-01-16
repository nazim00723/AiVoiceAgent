import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_response(prompt):
    try:
        # Use the new completion endpoint
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Replace with "gpt-3.5-turbo" if needed
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        # Extract the response text
        return response['choices'][0]['message']['content'].strip()

    except openai.error.OpenAIError as e:
        return f"Error communicating with OpenAI API: {e}"
