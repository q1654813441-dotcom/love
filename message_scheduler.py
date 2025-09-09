"""
消息调度模块
"""
import schedule
import time
from datetime import datetime
from wechat_api import WeChatAPI
from schedule_manager import ScheduleManager
from love_calculator import LoveCalculator
from period_tracker import PeriodTracker
from weather_api import WeatherAPI
from constellation_api import ConstellationAPI

class MessageScheduler:
    def __init__(self):
        self.wechat_api = WeChatAPI()
        self.schedule_manager = ScheduleManager()
        self.love_calculator = LoveCalculator()
        self.period_tracker = PeriodTracker()
        self.weather_api = WeatherAPI()
        self.constellation_api = ConstellationAPI()
    
    def generate_daily_message(self):
        """生成每日消息内容"""
        try:
            # 获取当前日期
            today = datetime.now()
            date_str = today.strftime('%Y年%m月%d日 %A')
            
            # 获取课程信息（极简）
            courses = self.schedule_manager.get_today_courses()
            if "有这些课：" in courses:
                courses_simple = courses.split("有这些课：")[1].strip()
                # 提取课程名称
                if "影视剧作" in courses_simple:
                    courses_simple = "影视剧作"
                elif "二维动画设计" in courses_simple:
                    courses_simple = "二维动画设计"
                elif "数字图像处理" in courses_simple:
                    courses_simple = "数字图像处理"
                elif "场景设计" in courses_simple:
                    courses_simple = "场景设计"
                elif "马克思主义基本原理" in courses_simple:
                    courses_simple = "马克思主义基本原理"
                elif "体育3" in courses_simple:
                    courses_simple = "体育3"
                elif "形势与政策" in courses_simple:
                    courses_simple = "形势与政策"
                elif "大学生创新创业基础" in courses_simple:
                    courses_simple = "大学生创新创业基础"
                elif "摄影摄像" in courses_simple:
                    courses_simple = "摄影摄像"
                elif "动画原理课程设计" in courses_simple:
                    courses_simple = "动画原理课程设计"
                else:
                    courses_simple = courses_simple[:10] if len(courses_simple) > 10 else courses_simple
            else:
                courses_simple = "无课" if "无课" in courses else "有课"
            
            # 获取恋爱信息（极简）
            love_days = self.love_calculator.get_love_days()
            love_info = f"在一起{love_days}天"
            
            # 获取大姨妈信息（极简）
            period_info = self.period_tracker.get_period_info()
            period_simple = "黄体期"
            if "预计" in period_info and "天后" in period_info:
                days = period_info.split("预计")[1].split("天后")[0]
                period_simple = f"{days}天后"
            elif "今天是" in period_info:
                period_simple = "经期"
            
            # 获取天气信息（极简）
            weather_data = self.weather_api.get_current_weather()
            weather_simple = weather_data['description'][:4] if len(weather_data['description']) > 4 else weather_data['description']
            temp_simple = weather_data['temperature']
            
            # 获取星座运势（详细版）
            fortune_data = self.constellation_api.get_daily_fortune()
            constellation_simple = f"狮子座今日运势：{fortune_data.get('summary', '运势不错')}"
            
            # 根据天气生成实用提示
            weather_desc = weather_data['description']
            temp_str = weather_data['temperature'].replace('°C', '')
            temp = int(temp_str) if temp_str.isdigit() else 25
            
            if '雨' in weather_desc:
                tips_simple = "记得带伞出门哦"
            elif '雪' in weather_desc:
                tips_simple = "下雪了，注意保暖"
            elif '晴' in weather_desc or '太阳' in weather_desc:
                tips_simple = "阳光明媚，适合外出"
            elif '云' in weather_desc or '阴' in weather_desc:
                tips_simple = "多云天气，注意防晒"
            elif '风' in weather_desc:
                tips_simple = "有风，注意发型"
            elif temp > 30:
                tips_simple = "天气炎热，多喝水"
            elif temp < 10:
                tips_simple = "天气较冷，记得穿外套"
            else:
                tips_simple = "天气不错，心情愉快"
            
            # 组合消息
            message_data = {
                'date': date_str,
                'weather': weather_simple,
                'temperature': temp_simple,
                'courses': courses_simple,
                'love_days': love_info,
                'period_info': period_simple,
                'constellation': constellation_simple,
                'tips': tips_simple
            }
            
            return message_data
            
        except Exception as e:
            print(f"生成每日消息失败: {e}")
            return None
    
    def send_daily_message(self):
        """发送每日消息"""
        print(f"[{datetime.now()}] 开始生成每日消息...")
        
        message_data = self.generate_daily_message()
        if message_data:
            success = self.wechat_api.send_daily_message(message_data)
            if success:
                print(f"[{datetime.now()}] 每日消息发送成功！")
            else:
                print(f"[{datetime.now()}] 每日消息发送失败！")
        else:
            print(f"[{datetime.now()}] 生成消息数据失败！")
    
    def test_message(self):
        """测试消息发送"""
        print("发送测试消息...")
        self.send_daily_message()
    
    def start_scheduler(self):
        """启动定时任务"""
        from config import PUSH_TIME
        
        # 设置定时任务
        schedule.every().day.at(PUSH_TIME).do(self.send_daily_message)
        
        print(f"定时任务已启动，每天 {PUSH_TIME} 发送消息")
        print("按 Ctrl+C 停止程序")
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # 每分钟检查一次
        except KeyboardInterrupt:
            print("\n程序已停止")
    
    def run_once(self):
        """立即运行一次（用于测试）"""
        self.send_daily_message()
