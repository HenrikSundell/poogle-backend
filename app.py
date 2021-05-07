from flask import Flask, request
import json
import requests
app = Flask(__name__)


@app.route('/')
def index():
    return "Setup"

def help(q):
    URL = "https://libretranslate.com/translate"
    lang = ["zh", "ar", "es", "de", "en"]
    source = "en"
    query = q
    for l in lang:
        data = {
        "q": query,
        "source": source ,
        "target": l
        }
        source = l
        response = requests.post(URL, data=json.dumps(data), headers={"Content-Type": "application/json"})
        print(query)
        query = response.json()["translatedText"]

    return query 






@app.route('/translate', methods=["GET"])
def translate():
    q = request.args.get('q', None)
    
    ans = help(q)

    return ans


if __name__ == "__main__":
    app.run(debug=False)