from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.user import User
from app.utils.nostr_auth import verify_nostr_auth, generate_auth_challenge
from app import db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('room.index'))
        
    if request.method == 'GET':
        # 生成认证挑战
        challenge = generate_auth_challenge()
        session['auth_challenge'] = challenge
        return render_template('login.html', challenge=challenge)
    
    # 处理POST请求
    event_data = request.json.get('signed_event')
    if not event_data:
        return jsonify({'error': '缺少签名事件'}), 400
        
    # 验证nostr事件
    pubkey = verify_nostr_auth(event_data)
    if not pubkey:
        return jsonify({'error': '验证失败'}), 400
        
    # 获取或创建用户
    user = User.get_by_pubkey(pubkey)
    if not user:
        user = User(pubkey=pubkey)
        db.session.add(user)
        db.session.commit()
    
    # 登录用户
    login_user(user)
    return jsonify({'success': True, 'redirect': url_for('room.index')})

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已成功退出登录')
    return redirect(url_for('auth.login'))

@bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html')
