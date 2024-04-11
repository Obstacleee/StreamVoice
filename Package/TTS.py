from pathlib import Path
from openai import OpenAI
OPENAI_API_KEY = "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"
client = OpenAI(
  api_key="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",
)




completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)
# speech_file_path = Path(__file__).parent / "speech.mp3"
# response = client.audio.speech.create(
#   model="tts-1",
#   voice="alloy",
#   input="Today is a wonderful day to build something people love!"
# )

# response.stream_to_file(speech_file_path)