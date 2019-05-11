from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, IntegerField
from wtforms.validators import DataRequired

class InfoForm(FlaskForm):
    title = StringField('Event name:', validators=[DataRequired()])
    question1 = StringField('Question 1:', validators=[DataRequired()])
    question2 = StringField('Question 2:', validators=[DataRequired()])
    question3 = StringField('Question 3:', validators=[DataRequired()])
    answer1 = StringField('Answers for 1:', validators=[DataRequired()])
    answer2 = StringField(validators=[DataRequired()])
    answer3 = StringField(validators=[DataRequired()])
    answer4 = StringField('Answers for 2:', validators=[DataRequired()])
    answer5 = StringField(validators=[DataRequired()])
    answer6 = StringField(validators=[DataRequired()])
    answer7 = StringField('Answers for 3:', validators=[DataRequired()])
    answer8 = StringField(validators=[DataRequired()])
    answer9 = StringField(validators=[DataRequired()])
    submit = SubmitField('Submit')
