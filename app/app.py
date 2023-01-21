from flask import Flask,render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    try:
        x = requests.get('https://w3schools.com')
        return render_template('index.html', status=x.status_code)
    except:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
