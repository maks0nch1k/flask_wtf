from flask import Flask, render_template, redirect, request
from loginform import LoginForm
import os
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/<title>")
@app.route("/index/<title>")
def ready(title):
    return render_template("base.html", title=title)


@app.route("/training/<prof>")
def training(prof):
    return render_template("training.html", title="training", prof=prof)


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


@app.route("/gallery", methods=["POST", "GET"])
def gallery():
    img_list = os.listdir(os.getcwd() + "/static/img")
    first_img = img_list[0]
    img_list = img_list[1:]
    if request.method == "GET":
        return render_template("gallery.html",
                               title="Красная планета",
                               img_list=img_list,
                               len_img_list=len(img_list) + 1,
                               first_img=first_img)
    elif request.method == "POST":
        img = request.files["file"]
        with open(f"static/img/{len(img_list) + 1}.png", "wb") as file:
            file.write(img.read())
        return redirect("/gallery")


@app.route("/table/<sex>/<int:age>")
def table(sex, age):
    return render_template("table.html", title="table", sex=sex, age=age)


@app.route("/member")
def member():
    with open("templates/member.json", encoding="UTF-8") as file:
        f = file.read()
        data = json.loads(f)
    return render_template("member.html", title="member", list_of_members=data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
