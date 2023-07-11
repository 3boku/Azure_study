from transformers import pipeline

nlp = pipeline("question-answering")
result = nlp(question="What is my name?", context="My name is John")

print(result)
answer = result['answer']
score = round(result['score'], 4)
print(f"answer: {answer}, score: {score}")