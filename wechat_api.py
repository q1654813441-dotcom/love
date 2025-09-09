"""
微信测试号API接口
"""
import requests
import json
from config import WECHAT_CONFIG

class WeChatAPI:
    def __init__(self):
        self.app_id = WECHAT_CONFIG['app_id']
        self.app_secret = WECHAT_CONFIG['app_secret']
        self.template_id = WECHAT_CONFIG['template_id']
        self.user_openid = WECHAT_CONFIG['user_openid']
        self.access_token = None
    
    def get_access_token(self):
        """获取access_token"""
        url = "https://api.weixin.qq.com/cgi-bin/token"
        params = {
            'grant_type': 'client_credential',
            'appid': self.app_id,
            'secret': self.app_secret
        }
        
        try:
            response = requests.get(url, params=params)
            data = response.json()
            
            if 'access_token' in data:
                self.access_token = data['access_token']
                print(f"获取access_token成功: {self.access_token[:20]}...")
                return True
            else:
                print(f"获取access_token失败: {data}")
                return False
        except Exception as e:
            print(f"获取access_token异常: {e}")
            return False
    
    def send_template_message(self, template_data):
        """发送模板消息"""
        if not self.access_token:
            if not self.get_access_token():
                return False
        
        url = f"https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={self.access_token}"
        
        data = {
            "touser": self.user_openid,
            "template_id": self.template_id,
            "data": template_data
        }
        
        try:
            response = requests.post(url, json=data)
            result = response.json()
            
            if result.get('errcode') == 0:
                print("消息发送成功！")
                return True
            else:
                print(f"消息发送失败: {result}")
                return False
        except Exception as e:
            print(f"发送消息异常: {e}")
            return False
    
    def send_daily_message(self, message_data):
        """发送每日消息"""
        template_data = {
            "date": {
                "value": message_data.get('date', ''),
                "color": "#173177"
            },
            "weather": {
                "value": message_data.get('weather', ''),
                "color": "#173177"
            },
            "temperature": {
                "value": message_data.get('temperature', ''),
                "color": "#173177"
            },
            "courses": {
                "value": message_data.get('courses', ''),
                "color": "#173177"
            },
            "love_days": {
                "value": message_data.get('love_days', ''),
                "color": "#FF69B4"
            },
            "period_info": {
                "value": message_data.get('period_info', ''),
                "color": "#FF69B4"
            },
            "constellation": {
                "value": message_data.get('constellation', ''),
                "color": "#FFD700"
            },
            "tips": {
                "value": message_data.get('tips', ''),
                "color": "#32CD32"
            }
        }
        
        return self.send_template_message(template_data)
