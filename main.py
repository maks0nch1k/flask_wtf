from flask import Flask, render_template, redirect
from loginform import LoginForm
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template("double_protection.html", title="Аварийный доступ", form=form)


@app.route("/distribution")
def distribution():
    return render_template("distribution.html", title="distribution")


@app.route("/gallery")
def gallery():
    img_list = os.listdir("C:/Users/79819/PycharmProjects/flask_wtf/static/img")
    return render_template("gallery.html", title="Красная планета", img_list=img_list)


@app.route("/table/<sex>/<int:age>")
def table(sex, age):
    return render_template("table.html", title="table", sex=sex, age=age)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
