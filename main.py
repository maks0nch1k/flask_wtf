from flask import Flask, render_template


app = Flask(__name__)


@app.route("/<title>")
@app.route("/index/<title>")
def ready(title):
    return render_template("base1.html", title=title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
