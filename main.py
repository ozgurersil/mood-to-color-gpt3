import os
import openai
from dotenv import load_dotenv, find_dotenv
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/getColor', methods=['GET'])
def get_answer():
    load_dotenv(find_dotenv())
    msg = request.args.get('msg')
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        engine="davinci",
        prompt="The CSS code for a color like " + msg + ":\n\nbackground-color: #",
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=[";"]
    )
    return jsonify(response.choices[0].text)


#app.run()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_answer("a breeze sadness")
