import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()                                   # reads .env into environment variables
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

MODEL = "gemini-2.5-flash"   # use the current Flash model name shown in Google AI Studio

prompt = "Explain what a Large Language Model is in two sentences for a 3rd-year engineering student."

start = time.perf_counter()
response = client.models.generate_content(model=MODEL, contents=prompt)
latency = time.perf_counter() - start

print(response.text)
print("-" * 40)
usage = response.usage_metadata
print(f"Input tokens : {usage.prompt_token_count}")
print(f"Output tokens: {usage.candidates_token_count}")
print(f"Latency      : {latency:.2f} s")