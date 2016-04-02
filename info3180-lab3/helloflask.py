import os
HOST=os.environ['IP']
PORT=os.environ['PORT']

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """<html><head></head><body>Hello World!"</body></html>"""

if __name__ == "__main__":
    app.run(host=HOST,port=PORT)

