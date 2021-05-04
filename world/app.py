from flask import Flask
from flask import render_template, flash, request,url_for
from wordclud import get_tweets
from forms import INPUTForm
from flask_bcrypt import Bcrypt
from flask import send_file

app  = Flask(__name__)
app.config['SECRET_KEY'] = '54321677890477655355TRGBJGFVF'


@app.route('/')
@app.route('/index')
def index():
    msg = 'Hello World!'

    return render_template('base.html', title='Home', msg=msg)



@app.route('/gtrends_wordcloud', methods=['GET', 'POST'])
def gen_gtrends_wordcloud():
    form = INPUTForm()
    if request.method == 'POST':
        image_str = get_tweets(form.maxtweet.data,form.trend.data,form.startdate.data,form.enddate.data)
        return render_template('gtrends_wc.html', title='Google Trends Wordcloud',
                               form=form, image=image_str)
    else:
        return render_template('gtrends_wc.html', title='Google Trends Wordcloud', form=form)

if __name__ == '__main__':
    app.run(debug=False)