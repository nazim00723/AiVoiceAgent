AI Voice Agent for Restaurant Booking 🎙️🍽️
Project Overview
This AI-powered voice agent automates restaurant booking calls by converting speech to text, generating responses using AI, and storing reservation details in a database. The system uses Deepgram API for speech-to-text, OpenAI API for response generation, and a MySQL database for managing reservations.

Features
✅ Speech-to-text transcription using Deepgram API
✅ AI-generated responses with OpenAI's GPT model
✅ Secure database storage for customer reservations
✅ Flask-based API for seamless communication
✅ Error handling and logging for better debugging

Tech Stack
🔹 Backend: Flask (Python)
🔹 APIs: Deepgram (STT), OpenAI (AI-generated responses)
🔹 Database: MySQL
🔹 Frontend: (Optional) Can integrate with a UI
🔹 Hosting: Can be deployed on AWS, Azure, or Heroku

Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/ai-voice-agent.git
cd ai-voice-agent

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Set Up API Keys
Create a .env file in the project root and add:
DEEPGRAM_API_KEY=your_deepgram_api_key
OPENAI_API_KEY=your_openai_api_key
DB_HOST=your_database_host
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=your_database_name

4️⃣ Run the Flask App
python app.py
The server will start at: http://127.0.0.1:5000

API Endpoints
🎤 Process Audio (Speech-to-Text & AI Response)
🔹 Endpoint: /process-audio
🔹 Method: POST
🔹 Body: Form-data with audio file

Example Request (Postman)
Upload an audio file (.mp3, .wav, .m4a)
Send a POST request
Response:
{
    "transcript": "I would like to book a table for 4 at 7 PM.",
    "response": "Your reservation for 4 people at 7 PM has been confirmed!"
}
📌 Book a Table (Store Reservation Details)
🔹 Endpoint: /book
🔹 Method: POST
🔹 Body: JSON
{
    "customer_name": "John Doe",
    "contact_number": "+1234567890",
    "reservation_time": "2024-01-20 19:00:00",
    "number_of_guests": 4
}

🔹 Response:
{
    "message": "Booking confirmed!"
}
Troubleshooting & Common Errors
🚨 Issue: "No audio file uploaded"
✔️ Solution: Ensure the audio file is sent as multipart/form-data in Postman.

🚨 Issue: "Error communicating with OpenAI API"
✔️ Solution: Check your OpenAI API Key and ensure your billing is active.

🚨 Issue: "Database connection failed"
✔️ Solution: Verify MySQL credentials in .env and ensure MySQL server is running.

Future Enhancements 🚀
🔹 Add a frontend UI for easy interaction
🔹 Implement multi-language support
🔹 Deploy on AWS/Azure for scalability


