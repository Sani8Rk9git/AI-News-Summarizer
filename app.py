from flask import Flask, render_template, request, jsonify
from utils.preprocess import (clean_text,extract_keywords,extract_entities)
from utils.summarize import summary
from utils.sentiment import senti
from utils.qa import answer


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/analyze",methods=["POST"])
def analyze():
    data = request.get_json()
    article = data["article"]

    article = clean_text(article)
    article_summary = summary(article)
    sentiment = senti(article)
    keywords = extract_keywords(article)
    entities = extract_entities(article)

    response = {
        "summary":article_summary,
        "sentiment":sentiment,
        "keywords":keywords,
        "entities": entities
    }

    return jsonify(response)

@app.route("/ask",methods=["POST"])
def answering():
    data = request.get_json()
    article = data["article"]
    userQuestion = data["question"]

    content = answer(userQuestion,article)

    return jsonify({
        "content":content
    })


if __name__ == "__main__":
    app.run(debug=True)

