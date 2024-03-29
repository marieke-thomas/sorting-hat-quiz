from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    model.reset_score()
    return render_template('index.html')

@app.route('/Q2', methods = ["GET", "POST"])
def q2():
    userdata = request.form
    # userdata = formopener.dict_from(request.form)
    model.add_points(userdata)
    return render_template('q2.html')

@app.route('/Q3', methods = ["GET", "POST"])
def q3():
    userdata = request.form
    # userdata = formopener.dict_from(request.form)
    model.add_points(userdata)
    return render_template('q3.html')

@app.route('/Q4', methods = ["GET", "POST"])
def q4():
    userdata = request.form
    # userdata = formopener.dict_from(request.form)
    model.add_points(userdata)
    return render_template('q4.html')

@app.route('/Q5', methods = ["GET", "POST"])
def q5():
    userdata = request.form
    model.add_points(userdata)
    return render_template('q5.html')

@app.route('/Q6', methods = ["GET", "POST"])
def q6():
    userdata = request.form
    model.add_points(userdata)
    return render_template('q6.html')

@app.route('/Q7', methods = ["GET", "POST"])
def q7():
    userdata = request.form
    model.add_points(userdata)
    return render_template('q7.html')

@app.route('/Q8', methods = ["GET", "POST"])
def q8():
    userdata = request.form
    model.add_points(userdata)
    return render_template('q8.html')

@app.route('/Q9', methods = ["GET", "POST"])
def q9():
    userdata = request.form
    model.add_points(userdata)
    return render_template('q9.html')

@app.route('/Q10', methods = ["GET", "POST"])
def q10():
    userdata = request.form
    model.add_points(userdata)
    return render_template('q10.html')

@app.route('/result', methods = ["GET", "POST"])
def result():
    userdata = request.form
    model.add_points(userdata)
    house = model.sort_user(userdata)
    print("You have been sorted into " + house)
    crest = model.pick_crest(house)
    return render_template('results.html',house = house,crest = crest)