from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Radit fuad asli from Jawir"

if __name__ == "__main__":
    app.run(debug=True)
