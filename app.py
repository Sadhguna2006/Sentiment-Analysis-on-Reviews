from flask import Flask, request, jsonify, render_template
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch

app = Flask(__name__)

model_path = "./sentiment_model_roberta"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
model.to(device)

sentiment_pipeline = pipeline(
    "sentiment-analysis", 
    model=model, 
    tokenizer=tokenizer, 
    device=0 if device.type != "cpu" else -1
)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    result = sentiment_pipeline(text)[0]

    if result["label"] == "LABEL_1":
        label = "positive"
    elif result["label"] == "LABEL_0":
        label = "negative"
    else:
        label = "neutral"

    score = result["score"]

    return jsonify({"label": label, "score": score})


if __name__ == '__main__':
    app.run(debug=True)
