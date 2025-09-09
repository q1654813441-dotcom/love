"""
天气查询模块 - 使用聚合数据API
"""
import requests
import json
from config import WEATHER_CONFIG

class WeatherAPI:
    def __init__(self):
        self.city = WEATHER_CONFIG['city']
        # 使用聚合数据天气API
        self.api_key = "a8535e8e97b46147ad50fba96ae9c523"
        self.base_url = "http://apis.juhe.cn/simpleWeather/query"
    
    def get_current_weather(self):
        """获取当前天气"""
        try:
            # 调用聚合数据天气API
            params = {
                'key': self.api_key,
                'city': self.city
            }
            
            response = requests.get(self.base_url, params=params, timeout=10)
            print(f"天气API响应状态: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"天气API响应: {data}")
                
                if data.get('error_code') == 0:
                    return self._parse_juhe_data(data)
                else:
                    print(f"聚合数据API错误: {data.get('reason', '未知错误')}")
                    return self._get_fallback_weather()
            else:
                print(f"天气API请求失败: {response.status_code}")
                return self._get_fallback_weather()
                
        except Exception as e:
            print(f"获取天气信息失败: {e}")
            return self._get_fallback_weather()
    
    def _parse_juhe_data(self, data):
        """解析聚合数据天气API响应"""
        try:
            result = data['result']
            realtime = result['realtime']
            
            temp = int(realtime.get('temperature'))
            humidity = realtime.get('humidity')
            info = realtime.get('info')
            direct = realtime.get('direct')
            power = realtime.get('power')
            
            weather_info = {
                'temperature': f"{temp}°C",
                'feels_like': f"体感温度 {temp}°C",  # 聚合数据没有体感温度，使用实际温度
                'description': info,
                'humidity': f"湿度 {humidity}%",
                'wind': f"{direct} {power}"
            }
            
            return weather_info
        except Exception as e:
            print(f"解析聚合数据失败: {e}")
            return self._get_fallback_weather()
    
    def _get_fallback_weather(self):
        """获取备用天气信息"""
        return {
            'temperature': "25°C",
            'feels_like': "体感温度 25°C",
            'description': "多云",
            'humidity': "湿度 70%",
            'wind': "东南风 3级"
        }
    
    def get_weather_tips(self, weather_data):
        """根据天气给出建议"""
        tips = []
        
        try:
            temp_str = weather_data['temperature'].replace('°C', '')
            temp = int(temp_str) if temp_str.isdigit() else 25
            description = weather_data['description'].lower()
            
            # 温度建议
            if temp < 0:
                tips.append("❄️ 天气很冷，记得穿厚一点，注意保暖")
            elif temp < 10:
                tips.append("🧥 天气较冷，建议穿外套")
            elif temp < 20:
                tips.append("👕 天气凉爽，适合穿长袖")
            elif temp < 30:
                tips.append("👔 天气舒适，可以穿薄外套")
            else:
                tips.append("☀️ 天气炎热，注意防暑降温")
            
            # 天气状况建议
            if '雨' in description:
                tips.append("☔ 今天有雨，记得带伞")
            elif '雪' in description:
                tips.append("❄️ 今天有雪，注意路面湿滑")
            elif '晴' in description:
                tips.append("☀️ 今天阳光明媚，适合外出")
            elif '云' in description or '阴' in description:
                tips.append("☁️ 今天多云，天气不错")
            elif '雾' in description:
                tips.append("🌫️ 今天有雾，出行注意安全")
            
            # 湿度建议
            if '湿度' in weather_data['humidity']:
                humidity_str = weather_data['humidity'].replace('湿度 ', '').replace('%', '')
                if humidity_str.isdigit():
                    humidity = int(humidity_str)
                    if humidity > 80:
                        tips.append("💧 湿度较高，注意防潮")
                    elif humidity < 30:
                        tips.append("💨 空气干燥，多喝水")
            
        except Exception as e:
            print(f"生成天气建议失败: {e}")
            tips.append("🌤️ 请关注天气变化，注意身体")
        
        return "\n".join(tips) if tips else "🌤️ 请关注天气变化，注意身体"