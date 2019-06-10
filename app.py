from flask import Flask, render_template, g, request
import sqlite3

app = Flask(__name__)


def connect_db():
    sql = sqlite3.connect('/home/nb/PycharmProjects/flask_food_tracker/foodlog.db')
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    if not hasattr(g, 'sqlite3.db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite3.db'):
        g.sqlite_db.close()


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/view')
def view():
    return render_template('day.html')


@app.route('/food', methods=['GET', 'POST'])
def food():
    if request.method == ['POST']:
        form = request.form
        return "Food: {}, Protein: {}, Carbs: {}, Fat:{}".format(form['food-name'], form['protein'], form['carbohydrates'], form['fat'])
    return render_template('add_food.html')


if __name__ == '__main__':
    app.run(debug=True)

