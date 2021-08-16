from flask import Flask, render_template, request, redirect, session
import random
from survey import Survey

app = Flask(__name__)
app.secret_key = 'Hello World'

@app.route('/')
def surveyHome():

    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submitSurvey():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    print(request.form)
    if not Survey.validate_survey(request.form):
        return redirect('/')
    Survey.create_survey(request.form)
    return redirect('/result')

@app.route('/result')
def results():
    return render_template('results.html', name = session['name'], location = session['location'], language = session['language'], comment = session['comment'])

if __name__=="__main__":
    app.run(debug=True)