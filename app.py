from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Flask based <b>Greeting</b> Application in Dockerized Environment'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5003)
