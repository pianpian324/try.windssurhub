from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.room import Room
from app.models.user import RoomOperation
from app import db

bp = Blueprint('room', __name__)

@bp.route('/')
@login_required
def index():
    rooms = Room.query.all()
    return render_template('index.html', rooms=rooms)

@bp.route('/add_room', methods=['GET', 'POST'])
@login_required
def add_room():
    if request.method == 'POST':
        number = request.form['number']
        room_type = request.form['type']
        price = float(request.form['price'])
        
        new_room = Room(number=number, type=room_type, price=price)
        db.session.add(new_room)
        
        # 记录操作
        operation = RoomOperation(
            room=new_room,
            operator=current_user,
            operation_type='create',
            new_value=f"房间号: {number}, 类型: {room_type}, 价格: {price}"
        )
        db.session.add(operation)
        
        db.session.commit()
        
        flash('房间添加成功！', 'success')
        return redirect(url_for('room.index'))
    
    return render_template('add_room.html')

@bp.route('/update_status/<int:room_id>', methods=['POST'])
@login_required
def update_status(room_id):
    room = Room.query.get_or_404(room_id)
    new_status = request.form['status']
    old_status = room.status
    room.status = new_status
    
    # 记录操作
    operation = RoomOperation(
        room=room,
        operator=current_user,
        operation_type='status_change',
        old_value=old_status,
        new_value=new_status
    )
    db.session.add(operation)
    
    db.session.commit()
    flash('房间状态已更新！', 'success')
    return redirect(url_for('room.index'))
