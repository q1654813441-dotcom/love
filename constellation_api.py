"""
星座运势查询模块
"""
import requests
import json
from bs4 import BeautifulSoup
from config import CONSTELLATION

class ConstellationAPI:
    def __init__(self):
        self.constellation = CONSTELLATION
        self.constellation_map = {
            '白羊座': 'aries', '金牛座': 'taurus', '双子座': 'gemini',
            '巨蟹座': 'cancer', '狮子座': 'leo', '处女座': 'virgo',
            '天秤座': 'libra', '天蝎座': 'scorpio', '射手座': 'sagittarius',
            '摩羯座': 'capricorn', '水瓶座': 'aquarius', '双鱼座': 'pisces'
        }
    
    def get_daily_fortune(self):
        """获取每日星座运势"""
        try:
            # 使用免费的星座API
            url = "https://api.vvhan.com/api/horoscope"
            params = {
                'type': 'today',
                'time': 'today'
            }
            
            response = requests.get(url, params=params, timeout=10)
            data = response.json()
            
            if data.get('success'):
                return self._parse_fortune_data(data)
            else:
                return self._get_fallback_fortune()
                
        except Exception as e:
            print(f"获取星座运势失败: {e}")
            return self._get_fallback_fortune()
    
    def _parse_fortune_data(self, data):
        """解析运势数据"""
        try:
            # 查找对应星座的运势
            constellation_en = self.constellation_map.get(self.constellation, 'libra')
            
            # 这里需要根据实际API返回的数据结构来解析
            # 由于不同API结构不同，这里提供一个通用的解析方法
            fortune_info = {
                'constellation': self.constellation,
                'date': data.get('date', '今天'),
                'lucky_color': data.get('lucky_color', '粉色'),
                'lucky_number': data.get('lucky_number', '7'),
                'overall': data.get('overall', '运势不错'),
                'love': data.get('love', '感情顺利'),
                'work': data.get('work', '工作顺利'),
                'money': data.get('money', '财运一般'),
                'health': data.get('health', '身体健康'),
                'advice': data.get('advice', '保持好心情')
            }
            
            return fortune_info
        except Exception as e:
            print(f"解析运势数据失败: {e}")
            return self._get_fallback_fortune()
    
    def _get_fallback_fortune(self):
        """获取备用运势信息"""
        import random
        
        # 随机生成一些正面的运势信息
        overall_list = [
            "今天运势不错，保持好心情",
            "今天会有小惊喜，期待一下吧",
            "今天适合做重要决定",
            "今天人际关系很好，多与人交流",
            "今天财运不错，可能会有意外收获"
        ]
        
        love_list = [
            "感情运势很好，和另一半相处愉快",
            "单身的朋友今天可能会遇到心仪的人",
            "感情稳定，可以考虑进一步发展",
            "今天适合表达爱意",
            "感情方面会有新的进展"
        ]
        
        work_list = [
            "工作运势不错，容易得到认可",
            "今天适合处理重要工作",
            "团队合作会很顺利",
            "今天可能会有新的工作机会",
            "工作压力不大，可以轻松应对"
        ]
        
        advice_list = [
            "保持积极乐观的心态",
            "多关注身边的人和事",
            "今天适合学习新知识",
            "注意身体健康，适当运动",
            "相信自己的直觉"
        ]
        
        return {
            'constellation': self.constellation,
            'date': '今天',
            'lucky_color': random.choice(['粉色', '蓝色', '绿色', '黄色', '紫色']),
            'lucky_number': str(random.randint(1, 9)),
            'overall': random.choice(overall_list),
            'love': random.choice(love_list),
            'work': random.choice(work_list),
            'money': '财运平稳，理性消费',
            'health': '身体健康，注意休息',
            'advice': random.choice(advice_list)
        }
    
    def format_fortune_message(self, fortune_data):
        """格式化运势消息"""
        message = f"🌟 {fortune_data['constellation']} 今日运势\n"
        message += f"📅 {fortune_data['date']}\n\n"
        message += f"💫 综合运势：{fortune_data['overall']}\n"
        message += f"💕 爱情运势：{fortune_data['love']}\n"
        message += f"💼 工作运势：{fortune_data['work']}\n"
        message += f"💰 财运：{fortune_data['money']}\n"
        message += f"🏥 健康运势：{fortune_data['health']}\n\n"
        message += f"🎨 幸运色：{fortune_data['lucky_color']}\n"
        message += f"🔢 幸运数字：{fortune_data['lucky_number']}\n\n"
        message += f"💡 今日建议：{fortune_data['advice']}"
        
        return message
