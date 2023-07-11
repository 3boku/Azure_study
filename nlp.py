from transformers import pipeline

nlp = pipeline("sentiment-analysis")
result = nlp("I love this movie")
label = result[0]['label']
score = round(result[0]['score'], 4)

print(result)
print(f"label: {label}, score: {score}")