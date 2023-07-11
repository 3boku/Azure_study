import gradio as gr


from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="sangrimlee/bert-base-multilingual-cased-nsmc")

def sentiment_analysis(text):
    result = classifier("액션이 화려하고 스토리도 좋았음")
    label = result[0]['label']
    return label

demo = gr.Interface(fn = sentiment_analysis, inputs="text", outputs="text", title="감정분석", description="텍스트를 입력하면 감정을 분석합니다.")

demo.launch(share=True)