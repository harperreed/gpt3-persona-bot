from flask import Flask, request, render_template
import logging
import argparse
from persona_bot import persona_bot

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
logging.info("Starting up bot")


parser = argparse.ArgumentParser(description=None)

parser.add_argument("-p", "--persona", default="guru")
args = parser.parse_args()
persona = args.persona

bot = persona_bot(persona_name=persona, log_level=logging.DEBUG)


@app.route('/get')
def bot_response(question=None):
    question = request.args.get("msg")
    logger.info("Q: " + question)
    response = bot.ask(question)
    logger.info("A: " + response)
    return response

@app.route('/')
def chat():
    
    # template largely based off of chatterbot python implementation
    # https://github.com/chamkank/flask-chatterbot
    return render_template('index.html', persona=bot.persona)



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
