"""Main script, uses other modules to generate sentences."""
from flask import Flask
import sample
import rearrange
import histogram
import random


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
    number_of_words = random.randint(5, 10)
    words = []
    for i in range(number_of_words):
        words.append(sample.weighted_random_word(new_histogram))

    shuffled = rearrange.rearrange_words(words)
    
    shuffled = shuffled.capitalize()
    sentence = shuffled + '.'

    return sentence
    


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
