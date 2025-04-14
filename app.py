from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    days = None
    birthdate_str = None

    if request.method == 'POST':
        birthdate_str = request.form.get('birthdate')
        if birthdate_str:
            birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
            today = datetime.today()
            delta = today - birthdate
            days = delta.days

    return render_template('index.html', days=days, birthdate=birthdate_str)

if __name__ == '__main__':
    app.run(debug=True)
