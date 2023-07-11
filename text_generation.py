from transformers import pipeline

nlp = pipeline("text-generation")
result = nlp("In a world")

print(result[0]['generated_text'])