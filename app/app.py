from flask import Flask

app = Flask(__name__)

@app.route("/blog")
def blog():
    return "Hello, This is a flask blog!!!"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True)