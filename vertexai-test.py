import vertexai
from vertexai.generative_models import GenerativeModel

vertexai.init(project="genai-hackathon-432810",
              location="us-central1")

model = GenerativeModel("gemini-1.5-flash-001")

response = model.generate_content(
    "Who is Virat Kohli"
)

print(response.text)