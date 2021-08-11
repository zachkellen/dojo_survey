from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'Hello World'

@app.route('/')
def surveyHome():

    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submitSurvey():
    print(request.form)
    session['name'] = request.form['full_name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def results():
    return render_template('results.html', name = session['name'], location = session['location'], language = session['language'], comment = session['comment'])

if __name__=="__main__":
    app.run(debug=True)