import json
from datetime import datetime, timedelta

def verify_nostr_auth(event_data):
    """验证nostr认证事件
    
    简化版本：仅验证事件格式和时间戳
    在生产环境中应该进行完整的签名验证
    """
    try:
        event = json.loads(event_data)
        
        # 验证事件格式
        required_fields = ['pubkey', 'created_at', 'content']
        if not all(field in event for field in required_fields):
            return None
            
        # 验证事件时间戳（5分钟内有效）
        event_time = datetime.fromtimestamp(event['created_at'])
        if datetime.utcnow() - event_time > timedelta(minutes=5):
            return None
            
        return event['pubkey']
    except Exception:
        return None

def generate_auth_challenge():
    """生成认证挑战"""
    timestamp = int(datetime.utcnow().timestamp())
    return f"Login to YinlinRoom at {timestamp}"
