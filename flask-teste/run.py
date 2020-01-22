from flask import Flask

app = Flask(__name__)
print("__name__ is ", __name__)
@app.route("/")
def index():
    return "<p style='color:red'>Hello World</p>"

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5001")