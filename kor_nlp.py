from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="sangrimlee/bert-base-multilingual-cased-nsmc")
result = classifier("액션이 화려하고 스토리도 좋았음")
label = result[0]['label']
score = round(result[0]['score'], 4)

print(f"label: {label}, score: {score}")