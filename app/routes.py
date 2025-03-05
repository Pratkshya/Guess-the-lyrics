from flask import render_template, request, url_for, flash, redirect
from flask import current_app as app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-lyrics', methods=['POST'])
def check_lyrics():
    user_lyrics = request.form['lyrics']
    correct_lyrics = "knowing that you love me"

    if user_lyrics.strip().lower() == correct_lyrics.strip().lower():
        return redirect(url_for('result', timestamp=40))
    else:
        flash("Incorrect lyrics. MOLE")
        return redirect(url_for('index'))

@app.route('/result')
def result():
    timestamp = request.args.get('timestamp', 0)
    return render_template('result.html', timestamp=timestamp)