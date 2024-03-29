from flask import Flask
import os
import time

app = Flask(__name__)

@app.route('/')
def hello():
    print("Request coming in, sleep for 110 second")
    time.sleep(110)
    return "Hello World!"

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)
    print("enter into the main")

    app.run(port=port,host='0.0.0.0')
