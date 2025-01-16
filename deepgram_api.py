from deepgram import Deepgram
import asyncio
from config import DEEPGRAM_API_KEY

deepgram = Deepgram(DEEPGRAM_API_KEY)

def transcribe_audio(audio_path):
    async def main():
        with open(audio_path, 'rb') as audio:
            # Add the required keys: 'buffer' and 'mimetype'
            response = await deepgram.transcription.prerecorded(
                {"buffer": audio, "mimetype": "audio/wav"},  # Replace "audio/wav" with your file type if different
                {"punctuate": True}
            )
            return response["results"]["channels"][0]["alternatives"][0]["transcript"]

    return asyncio.run(main())
