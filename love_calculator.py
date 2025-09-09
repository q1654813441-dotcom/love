"""
恋爱天数计算模块
"""
from datetime import datetime, timedelta
from config import LOVE_START_DATE, GIRLFRIEND_BIRTHDAY

class LoveCalculator:
    def __init__(self):
        self.start_date = LOVE_START_DATE
        self.girlfriend_birthday = GIRLFRIEND_BIRTHDAY
    
    def get_love_days(self):
        """计算恋爱天数"""
        today = datetime.now()
        delta = today - self.start_date
        return delta.days
    
    def get_love_info(self):
        """获取恋爱信息"""
        days = self.get_love_days()
        years = days // 365
        months = (days % 365) // 30
        remaining_days = days % 30
        
        info = f"我们已经在一起 {days} 天了！"
        
        if years > 0:
            info += f"\n也就是 {years} 年"
        if months > 0:
            info += f" {months} 个月"
        if remaining_days > 0:
            info += f" {remaining_days} 天"
        
        # 添加一些特殊日子的提醒
        if days % 100 == 0:
            info += f"\n🎉 恭喜！今天是我们恋爱的第 {days} 天纪念日！"
        elif days % 30 == 0:
            info += f"\n💕 我们又一起走过了 {days//30} 个月！"
        elif days % 7 == 0:
            info += f"\n💖 这周是我们恋爱的第 {days//7} 周！"
        
        return info
    
    def get_next_anniversary(self):
        """获取下一个纪念日"""
        today = datetime.now()
        current_year = today.year
        
        # 计算今年的纪念日
        this_year_anniversary = datetime(current_year, self.start_date.month, self.start_date.day)
        
        if today < this_year_anniversary:
            # 今年的纪念日还没到
            next_anniversary = this_year_anniversary
        else:
            # 今年的纪念日已经过了，计算明年的
            next_anniversary = datetime(current_year + 1, self.start_date.month, self.start_date.day)
        
        days_to_anniversary = (next_anniversary - today).days
        return f"距离我们的恋爱纪念日还有 {days_to_anniversary} 天！"
    
    def get_birthday_info(self):
        """获取生日信息"""
        today = datetime.now()
        current_year = today.year
        
        # 计算今年的生日
        this_year_birthday = datetime(current_year, self.girlfriend_birthday.month, self.girlfriend_birthday.day)
        
        if today < this_year_birthday:
            # 今年的生日还没到
            next_birthday = this_year_birthday
            age = current_year - self.girlfriend_birthday.year
        else:
            # 今年的生日已经过了，计算明年的
            next_birthday = datetime(current_year + 1, self.girlfriend_birthday.month, self.girlfriend_birthday.day)
            age = current_year - self.girlfriend_birthday.year + 1
        
        days_to_birthday = (next_birthday - today).days
        
        if days_to_birthday == 0:
            return f"🎉 今天是宝贝的生日！生日快乐！🎂"
        elif days_to_birthday == 1:
            return f"🎂 明天是宝贝的生日！准备惊喜吧！"
        elif days_to_birthday <= 7:
            return f"🎂 还有 {days_to_birthday} 天就是宝贝的生日了！"
        else:
            return f"🎂 宝贝的生日是 {self.girlfriend_birthday.month}月{self.girlfriend_birthday.day}日，还有 {days_to_birthday} 天"
    
    def get_age(self):
        """计算女朋友年龄"""
        today = datetime.now()
        age = today.year - self.girlfriend_birthday.year
        
        # 如果今年的生日还没到，年龄减1
        if today.month < self.girlfriend_birthday.month or \
           (today.month == self.girlfriend_birthday.month and today.day < self.girlfriend_birthday.day):
            age -= 1
        
        return age
