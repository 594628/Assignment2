import app
from flask import Flask, render_template, session, redirect, url_for, request
from predict import predict, get_form_data
from forms import DataForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def index():


    form = DataForm()

    if form.validate_on_submit():

        for fieldname, value in form.data.items():
            session[fieldname] = value

        pred = predict(session)
        session['pred'] = pred

        # Get additional user data
        #user_info = request.headers.get('User-Agent')

        # Preprocess data
        #data = get_form_data(session)

        # Get model outputs
        #pred = predict(data)

        # Create the payload (we use session)
        #session['user_info'] = user_info
        #session['pred'] = pred

        return redirect(url_for('index'))

    return render_template('index.html', form=form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


