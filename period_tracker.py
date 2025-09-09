"""
大姨妈提醒模块
"""
from datetime import datetime, timedelta
from config import PERIOD_CONFIG

class PeriodTracker:
    def __init__(self):
        self.cycle_days = PERIOD_CONFIG['cycle_days']
        self.last_period_date = PERIOD_CONFIG['last_period_date']
        self.period_days = PERIOD_CONFIG['period_days']
    
    def get_period_info(self):
        """获取大姨妈相关信息"""
        today = datetime.now()
        days_since_last = (today - self.last_period_date).days
        
        # 计算下次月经预计日期
        next_period_date = self.last_period_date + timedelta(days=self.cycle_days)
        days_to_next = (next_period_date - today).days
        
        # 计算当前周期天数
        current_cycle_day = days_since_last % self.cycle_days
        if current_cycle_day == 0:
            current_cycle_day = self.cycle_days
        
        info = f"上次月经：{self.last_period_date.strftime('%Y-%m-%d')}\n"
        info += f"距离上次：{days_since_last} 天\n"
        info += f"当前周期：第 {current_cycle_day} 天\n"
        
        if days_to_next <= 3 and days_to_next > 0:
            info += f"⚠️ 预计 {days_to_next} 天后月经来潮，记得准备卫生用品！"
        elif days_to_next <= 0:
            info += f"📅 预计月经日期已过，如果还没来请关注身体状况"
        elif days_to_next <= 7:
            info += f"💡 还有 {days_to_next} 天就到月经期了，注意休息"
        else:
            info += f"✅ 距离下次月经还有 {days_to_next} 天，保持好心情"
        
        # 添加经期护理建议
        if 1 <= current_cycle_day <= self.period_days:
            info += f"\n🩸 当前是经期第 {current_cycle_day} 天，注意保暖和休息"
        elif 8 <= current_cycle_day <= 14:
            info += f"\n🌸 现在是排卵期，注意个人卫生"
        elif 15 <= current_cycle_day <= 21:
            info += f"\n💪 现在是黄体期，保持规律作息"
        else:
            info += f"\n🌙 现在是卵泡期，保持好心情"
        
        return info
    
    def update_last_period_date(self, new_date):
        """更新上次月经日期"""
        self.last_period_date = new_date
    
    def get_cycle_analysis(self):
        """获取周期分析"""
        today = datetime.now()
        days_since_last = (today - self.last_period_date).days
        
        # 简单的周期分析
        if days_since_last < self.cycle_days - 7:
            return "周期正常，保持规律作息"
        elif days_since_last < self.cycle_days:
            return "接近月经期，注意身体变化"
        elif days_since_last == self.cycle_days:
            return "预计月经期，做好准备"
        else:
            return "月经期已过，注意观察身体恢复情况"
