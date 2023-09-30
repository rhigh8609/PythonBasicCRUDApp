# Import necessary modules from the Flask library
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exercises.db'
db = SQLAlchemy(app)

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

with app.app_context():
    db.create_all()

@app.route('/add', methods=['POST'])
def add_exercise():
    name = request.form.get('name')
    weight = float(request.form.get('weight'))
    reps = int(request.form.get('reps'))
    date = datetime.strptime(request.form.get('date'), '%Y-%m-%d') if request.form.get('date') else None

    if name and weight and reps:
        new_exercise = Exercise(name=name, weight=weight, reps=reps, date=date if date else datetime.utcnow())
        db.session.add(new_exercise)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/')
def index():
    exercises = Exercise.query.all()
    return render_template('index.html', exercises=exercises)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    if request.method == 'POST':
        exercise.name = request.form.get('name')
        exercise.weight = float(request.form.get('weight'))
        exercise.reps = int(request.form.get('reps'))
        exercise.date = datetime.strptime(request.form.get('date'), '%Y-%m-%d') if request.form.get('date') else exercise.date
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', exercise=exercise)

@app.route('/delete/<int:id>')
def delete_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    db.session.delete(exercise)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
