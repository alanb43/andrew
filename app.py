from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    
    return render_template('index.html', title="Teaching Andrew", name="by Alan")


@app.route("/andrew")
def andrew():
    
    return render_template('index.html', title="", name="")

if __name__ == "__main__":
    app.run()

