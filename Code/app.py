"""Main script, uses other modules to generate sentences."""
from flask import Flask, request, redirect
import sample
import rearrange
import histogram
import random
import twitter 
import markov

app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.
def source_text():
    with open('dnd5esrd.txt', 'r') as f:
        return f.read().replace('\n', ' ')
        
source = source_text()

new_histogram = histogram.histogram(source)

@app.route("/")
def home():
    markov_chain = markov.MarkovChain(source)
    sentence = markov_chain.generate_sentence()
    return sentence

@app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['sentence']
    twitter.tweet(status)
    return redirect('/')
    


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
