from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route("/")
def function1():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)