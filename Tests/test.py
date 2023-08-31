# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text2text-generation", model="HarshSinyal/Constitution-India-Falcon-Sharded-7B")

# Load model directly
from transformers import AutoModel
model = AutoModel.from_pretrained("HarshSinyal/Constitution-India-Falcon-Sharded-7B")

example = "What are my Civil Rights according to the Consitution from Article 12 - 30"

results = pipe(example)
print(results)
