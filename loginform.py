from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_astronaut = StringField('Id астронавта', validators=[DataRequired()])
    pass_astronaut = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_leader = StringField('Id капитана', validators=[DataRequired()])
    pass_leader = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField("Доступ")