"""
配置文件
"""
import os
from datetime import datetime

# 微信测试号配置
WECHAT_CONFIG = {
    'app_id': os.getenv('WECHAT_APP_ID', 'wx4bce032616c5d598'),
    'app_secret': os.getenv('WECHAT_APP_SECRET', '65201a5d86e8292350850ea51960040e'),
    'template_id': os.getenv('WECHAT_TEMPLATE_ID', 'wC6BYEM-wNW5Agumfqm1_XQyEfAfM9orHh7AyloHt7k'),
    'user_openid': os.getenv('WECHAT_USER_OPENID', 'oEBD511jdtj1vPOjffxvHbYliEmM')
}

# 天气API配置
WEATHER_CONFIG = {
    'api_key': os.getenv('WEATHER_API_KEY', 'f1adf8bbfb2c4a959da2af37d278eb99'),
    'key_id': os.getenv('WEATHER_KEY_ID', 'TC5BTDMYMP'),
    'city': os.getenv('WEATHER_CITY', '福州')  # 可以修改为你的城市
}

# 星座配置
CONSTELLATION = os.getenv('CONSTELLATION', '狮子座')  # 你女朋友的星座

# 恋爱纪念日
LOVE_START_DATE = datetime(2025, 5, 16)  # 修改为你们开始恋爱的日期

# 女朋友生日
GIRLFRIEND_BIRTHDAY = datetime(2006, 7, 26)  # 女朋友生日

# 大姨妈配置
PERIOD_CONFIG = {
    'cycle_days': 30,  # 月经周期天数（每月23号左右）
    'last_period_date': datetime(2024, 12, 23),  # 上次月经开始日期（最近一次23号）
    'period_days': 5  # 月经持续天数
}

# 课程表配置 (按星期几配置，1-7代表周一到周日)
# 学期开始日期：2025年9月1日，共20周
SCHEDULE = {
    1: [],  # 周一 - 根据课表，周一没有固定课程
    2: [],  # 周二 - 根据课表，周二没有固定课程  
    3: [],  # 周三 - 根据课表，周三没有固定课程
    4: [],  # 周四 - 根据课表，周四没有固定课程
    5: [],  # 周五 - 根据课表，周五没有固定课程
    6: [],  # 周六
    7: []   # 周日
}


# 学期配置
SEMESTER_CONFIG = {
    'start_date': '2025-09-01',  # 学期开始日期
    'total_weeks': 20,  # 总周数
    'current_week': 1  # 当前周次（需要根据实际日期计算）
}

# 推送时间配置
PUSH_TIME = "08:00"  # 每天早上8点推送
