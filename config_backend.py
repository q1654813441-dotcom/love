"""
后台配置文件 - 需要填写的参数
请根据实际情况填写以下配置信息
"""

# ==================== 微信测试号配置 ====================
# 1. 访问 https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=jsapisign
# 2. 获取以下信息并填入

WECHAT_CONFIG = {
    'app_id': 'wx4bce032616c5d598',          # 微信测试号AppID
    'app_secret': '65201a5d86e8292350850ea51960040e',  # 微信测试号AppSecret
    'template_id': 'wC6BYEM-wNW5Agumfqm1_XQyEfAfM9orHh7AyloHt7k',  # 模板消息ID
    'user_openid': 'oEBD511jdtj1vPOjffxvHbYliEmM'   # 你女朋友的OpenID
}

# ==================== 天气API配置 ====================
# 使用和风天气API

WEATHER_CONFIG = {
    'api_key': 'f1adf8bbfb2c4a959da2af37d278eb99',  # 和风天气API密钥
    'key_id': 'TC5BTDMYMP',                          # 和风天气凭据ID
    'city': '北京'                                   # 城市名称（可修改）
}

# ==================== 个人信息配置 ====================
CONSTELLATION = '狮子座'                      # 你女朋友的星座

# ==================== 恋爱纪念日配置 ====================
# 修改为你们开始恋爱的日期
LOVE_START_DATE = '2025-05-16'               # 格式：YYYY-MM-DD

# ==================== 女朋友生日配置 ====================
GIRLFRIEND_BIRTHDAY = '2006-07-26'           # 女朋友生日 YYYY-MM-DD

# ==================== 大姨妈配置 ====================
PERIOD_CONFIG = {
    'cycle_days': 30,                         # 月经周期天数（每月23号左右）
    'last_period_date': '2024-12-23',         # 上次月经开始日期 YYYY-MM-DD（最近一次23号）
    'period_days': 5                          # 月经持续天数
}

# ==================== 推送时间配置 ====================
PUSH_TIME = "08:00"                          # 每天推送时间（24小时制）

# ==================== 学期配置 ====================
SEMESTER_CONFIG = {
    'start_date': '2025-09-01',              # 学期开始日期 YYYY-MM-DD
    'total_weeks': 20,                        # 总周数
}

# ==================== 课程表配置 ====================
# 课程表已根据你的课表自动配置，如需修改请编辑 schedule_manager.py 文件

# ==================== 宝塔面板部署配置 ====================
# 以下配置用于宝塔面板部署
DEPLOY_CONFIG = {
    'port': 8080,                            # 服务端口
    'host': '0.0.0.0',                       # 监听地址
    'debug': False,                          # 生产环境设为False
    'log_level': 'INFO'                      # 日志级别
}
