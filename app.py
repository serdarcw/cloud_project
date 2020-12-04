from flask import Flask, render_template, request, url_for
from covid19 import info_covid

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def enter():
    return render_template('enter.html')

@app.route('/login', methods=['POST','GET'])
def index():
    try:
        if request.method =='POST':
            country = request.form['infos']
            covid = info_covid(country)
            return render_template('index.html', results=covid)
        else:
            return render_template('index.html')
    except:
        return render_template('error.html')

@app.route('/aboutCovid', methods=['GET'])
def about():
    return render_template('about.html')

if __name__=='__main__':
    #app.run()
    #app.run(debug=True)
    app.run('0.0.0.0',port=80)


