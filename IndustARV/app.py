from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contributor')
def contributor():
    return render_template('contributor.html')

@app.route('/executive')
def executive():
    return render_template('executive.html')

@app.route('/work-list')
def work_list():
    return render_template('work_list.html')

@app.route('/solutions')
def solutions():
    return render_template('solutions.html')

if __name__ == '__main__':
    app.run(debug=True)
