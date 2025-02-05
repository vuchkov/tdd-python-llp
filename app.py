from flask import Flask, render_template, request
import json
import spacy
from llp_client import NamedEntityClient

app = Flask(__name__)

llp = spacy.load("en_core_web_sm")
llp = NamedEntityClient(llp)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/llp', methods=['POST'])
def get_named_ents():
    data = request.get_json()
    result = llp.get_ents(data["sentence"])
    response = { "entities": result.get('ents'), "html": result.get('html') }
    return json.dumps(response)

if __name__ == "__main__":
    app.run(debug=True)