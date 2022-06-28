from flask import Flask, json, render_template
app = Flask(__name__)
import logging

@app.route("/")
def index():
    app.logger.info('load index successful')
    return render_template('login.html')

if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')
    