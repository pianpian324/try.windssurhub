from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # 请在生产环境中更改此密钥
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guesthouse.db'
db = SQLAlchemy(app)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(10), unique=True, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='available')  # available, occupied, maintenance
    
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    rooms = Room.query.all()
    return render_template('index.html', rooms=rooms)

@app.route('/add_room', methods=['GET', 'POST'])
def add_room():
    if request.method == 'POST':
        number = request.form['number']
        room_type = request.form['type']
        price = float(request.form['price'])
        
        new_room = Room(number=number, type=room_type, price=price)
        db.session.add(new_room)
        db.session.commit()
        
        flash('房间添加成功！', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_room.html')

@app.route('/update_status/<int:room_id>', methods=['POST'])
def update_status(room_id):
    room = Room.query.get_or_404(room_id)
    new_status = request.form['status']
    room.status = new_status
    db.session.commit()
    flash('房间状态已更新！', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
