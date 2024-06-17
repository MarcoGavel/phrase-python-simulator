from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# List of random phrases
phrases = [
    "Bite off more than you can chew, then chew it.",
    "When life gives you lemons, squeeze them in people's eyes.",
    "Kick ass, take names, and never look back.",
    "Don't just break the mold, shatter it into a million pieces.",
    "Be the storm that no one saw coming.",
    "The world is your oyster, crack it wide open.",
    "Grab life by the horns and never let go.",
    "If you want something done right, do it with both barrels blazing.",
    "The early bird gets the worm, but the second mouse gets the cheese.",
    "Don't just turn heads, spin them.",
    "When the going gets tough, the tough go nuclear.",
    "Dream big, hustle hard, and make no apologies.",
    "Rise and grind, because sleep is for the weak.",
    "Play the game like you own the field.",
    "Blaze your own trail, even if it burns the forest down.",
    "Run with the wolves, and lead the pack.",
    "Fight like you're the third monkey trying to get on Noah's Ark.",
    "Don't wait for opportunity. Create it with a sledgehammer.",
    "Leave no stone unturned and no bridge unburned.",
    "When in doubt, make it loud and make it proud."
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        phrase = random.choice(phrases)
        return render_template('index.html', name=name, phrase=phrase)
    return render_template('index.html', name=None, phrase=None)

@app.route('/clear', methods=['GET', 'POST'])
def clear():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
