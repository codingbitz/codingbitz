from flask import render_template, request, redirect, url_for, flash, session, g
from pkgtt import db
from pkgtt.models import Blearn
from pkgtt import create_app
import os
from datetime import datetime
from sqlalchemy.sql import func

config_name = os.getenv('FLASK_ENV')
app = create_app(config_name)

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'badri' and request.form['password'] == 'badransan':
            session['badri'] = request.form['username']
            return redirect(url_for('index'))
        else:
            error = 'Invalid Credentials. Please try again.'

    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('login'))

@app.route('/index', methods=['GET', 'POST'])
def index():
    if session.get('logged_in') == False:
        print("Login again")
        return redirect(url_for('login'))
    else:
        all_data = Blearn.query.order_by((Blearn.learn_id.desc()))
        return render_template("index.html", blearn=all_data)


# this route is for inserting data to mysql database via forms
@app.route('/insert', methods=['POST'])
def insert():
    try:
        if request.method == 'POST':
            learn_date = request.form['learn_date']
            learn_start_time = request.form['learn_start_time']
            learn_end_time = request.form['learn_end_time']
            area_of_study = request.form['area_of_study']
            sub_area = request.form['sub_area']
            completion_status = request.form['completion_status']
            learning_src = request.form['learning_src']
            brief_desc = request.form['brief_desc']
            comments = request.form['comments']
            code_practice_link = request.form['code_practice_link']

            my_data = Blearn(learn_date, learn_start_time, learn_end_time, area_of_study, sub_area, completion_status,
                         learning_src, brief_desc, comments, code_practice_link)
            db.session.add(my_data)
            db.session.commit()
            flash("New Learning Data Inserted Successfully")

            return redirect(url_for('index'))
    except Exception as typErr:
        print("Error while inserting: ",typErr)


# this route is for updating data to mysql database via forms

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = Blearn.query.get(request.form.get('learn_id'))
        my_data.learn_date = request.form['learn_date']
        my_data.learn_start_time = request.form['learn_start_time']
        my_data.learn_end_time = request.form['learn_end_time']
        my_data.area_of_study = request.form['area_of_study']
        my_data.sub_area = request.form['sub_area']
        my_data.completion_status = request.form['completion_status']
        my_data.learning_src = request.form['learning_src']
        my_data.brief_desc = request.form['brief_desc']
        my_data.comments = request.form['comments']
        my_data.code_practice_link = request.form['code_practice_link']
        db.session.commit()

    flash("Learning Data Updated Successfully")
    return redirect(url_for('index'))


# this route is for deleting data to mysql database
@app.route('/delete/<learn_id>', methods=['GET', 'POST'])
def delete(learn_id):
    my_data = Blearn.query.get(learn_id)
    db.session.delete(my_data)
    db.session.commit()

    flash("Learning Data Deleted Successfully")
    return redirect(url_for('index'))
