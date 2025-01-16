from flask import Flask, request, jsonify
from deepgram_api import transcribe_audio
from openai_api import generate_response
from db_connection import get_db_connection
import os
import uuid

app = Flask(__name__)

@app.route("/process-audio", methods=["POST"])
def process_audio():
    # Check if the request contains files
    if not request.files:
        return jsonify({"error": "No files in request"}), 400

    # Debug: Print available files in the request
    print(f"Files in request: {request.files.keys()}")

    # Ensure the request contains an audio file
    if "audio" not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400

    file = request.files["audio"]

    if file.filename == "":
        return jsonify({"error": "Invalid file name"}), 400

    # Specify the directory to save audio files
    save_dir = r"C:\Users\chuna\OneDrive\Desktop\AiVoiceAgent"

    # Ensure the directory exists
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Define a unique filename
    unique_filename = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(save_dir, unique_filename)

    try:
        # Save the file to the specified location
        file.save(file_path)
    except Exception as e:
        return jsonify({"error": f"Error saving file: {str(e)}"}), 500

    try:
        # Step 1: Transcribe audio
        transcript = transcribe_audio(file_path)

        # Step 2: Generate response
        response = generate_response(transcript)

        return jsonify({"transcript": transcript, "response": response})
    except Exception as e:
        return jsonify({"error": f"Processing error: {str(e)}"}), 500

@app.route("/book", methods=["POST"])
def book_table():
    try:
        data = request.get_json()

        # Validate JSON data
        required_keys = ["customer_name", "contact_number", "reservation_time", "number_of_guests"]
        for key in required_keys:
            if key not in data:
                return jsonify({"error": f"Missing key: {key}"}), 400

        customer_name = data["customer_name"]
        contact_number = data["contact_number"]
        reservation_time = data["reservation_time"]
        number_of_guests = data["number_of_guests"]

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO bookings (customer_name, contact_number, reservation_time, number_of_guests) VALUES (%s, %s, %s, %s)",
            (customer_name, contact_number, reservation_time, number_of_guests)
        )
        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"message": "Booking confirmed!"})
    except Exception as e:
        return jsonify({"error": f"Error booking table: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
