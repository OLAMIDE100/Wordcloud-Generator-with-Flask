from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import DataRequired,Length,ValidationError
from wordclud import get_tweets


class INPUTForm(FlaskForm):
    maxtweet = IntegerField('Maximum Tweets',
                           validators=[DataRequired(),
                                       Length(min =2,max=20)])


    trend = StringField('Trend',
                           validators=[DataRequired(),
                                       Length(min =2,max=20)])

    startdate = StringField('Startdate',
                           validators=[DataRequired(),
                                       Length(min =2,max=20)])


    enddate = StringField('Enddate',
                           validators=[DataRequired(),
                                       Length(min =2,max=20)])
    
    
    submit = SubmitField('Generate')


