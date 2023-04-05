from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<title>")
@app.route("/index/<title>")
def ready(title):
    return render_template("base.html", title=title)


@app.route("/list_prof/<param>")
def jobs_list(param):
    jobs = ["инженер-исследователь",
            "пилот",
            "строитель",
            "экзобиолог",
            "врач",
            "инженер по терраформированию",
            "климатолог",
            "специалист по радиационной защите",
            "астрогеолог",
            "гляциолог",
            "инженер жизнеобеспечения",
            "метеоролог",
            "оператор марсохода",
            "киберинженер",
            "штурман",
            "пилот дронов"]

    return render_template("list_prof.html", jobs=jobs, param=param)


@app.route("/answer")
@app.route("/auto_answer")
def auto_ans():
    values = {"title": "Анкета",
              "surname": "Watny",
              "name": "Mark",
              "education": "выше среднего",
              "profession": "штурман марсохода",
              "sex": "male",
              "motivation": "Всегда мечтал застрять на марсе!",
              "ready": True}

    return render_template("auto_answer.html", **values)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
