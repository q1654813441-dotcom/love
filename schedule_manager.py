"""
课程表管理模块
"""
from datetime import datetime, timedelta
from config import SEMESTER_CONFIG

class ScheduleManager:
    def __init__(self):
        self.semester_start = datetime.strptime(SEMESTER_CONFIG['start_date'], '%Y-%m-%d')
        self.total_weeks = SEMESTER_CONFIG['total_weeks']
        
        # 根据详细课表信息配置的课程安排
        self.course_schedule = {
            # 周一 (Day I)
            1: {
                'morning_1_2': [
                    {'name': '动画原理课程设计', 'weeks': (17, 17), 'room': 'CX306'}
                ],
                'morning_3_5': [
                    {'name': '二维动画设计', 'weeks': (9, 16), 'room': 'CX306'}
                ],
                'afternoon_6_7': [
                    {'name': '二维动画设计', 'weeks': (9, 16), 'room': 'CX306'}
                ]
            },
            # 周二 (Day II)
            2: {
                'morning_1_2': [
                    {'name': '大学生创新创业基础', 'weeks': (10, 17), 'room': 'F202'}
                ],
                'morning_3_5': [
                    {'name': '影视剧作', 'weeks': (1, 6), 'room': 'B404'},
                    {'name': '摄影摄像', 'weeks': (7, 12), 'room': 'A202'}
                ],
                'afternoon_6_7': []
            },
            # 周三 (Day III)
            3: {
                'morning_1_2': [],
                'morning_3_5': [
                    {'name': '数字图像处理', 'weeks': (1, 10), 'room': 'CX210'},
                    {'name': '场景设计', 'weeks': (11, 18), 'room': 'CX309'}
                ],
                'afternoon_6_7': [
                    {'name': '数字图像处理', 'weeks': (1, 9), 'room': 'S110'},
                    {'name': '场景设计', 'weeks': (11, 18), 'room': 'CX309'}
                ]
            },
            # 周四 (Day IV)
            4: {
                'morning_1_2': [
                    {'name': '形势与政策', 'weeks': (10, 11), 'room': 'A101'}
                ],
                'morning_3_5': [
                    {'name': '影视剧作', 'weeks': (1, 5), 'room': 'C206'},
                    {'name': '摄影摄像', 'weeks': (7, 11), 'room': 'S201'}
                ],
                'afternoon_6_7': [
                    {'name': '体育3', 'weeks': (1, 11), 'room': '操场10'}
                ]
            },
            # 周五 (Day V)
            5: {
                'morning_1_2': [],
                'morning_3_5': [
                    {'name': '马克思主义基本原理', 'weeks': (1, 14), 'room': 'B404'}
                ],
                'afternoon_6_7': [],
                'evening_10_12': []
            }
        }
    
    def get_current_week(self):
        """获取当前是第几周"""
        today = datetime.now()
        if today < self.semester_start:
            return 0  # 学期还没开始
        
        days_diff = (today - self.semester_start).days
        current_week = (days_diff // 7) + 1
        
        return min(current_week, self.total_weeks)
    
    def is_course_in_week(self, course_weeks, current_week):
        """判断课程是否在当前周"""
        start_week, end_week = course_weeks
        return start_week <= current_week <= end_week
    
    def get_today_courses(self):
        """获取今天的课程"""
        today = datetime.now()
        weekday = today.weekday() + 1  # 转换为1-7格式（周一到周日）
        current_week = self.get_current_week()
        
        if weekday > 5:  # 周六周日
            return "今天是周末，没有课，好好休息吧~"
        
        if current_week == 0:
            return "学期还没开始，好好享受假期吧~"
        
        if current_week > self.total_weeks:
            return "学期已经结束，恭喜你完成了这学期的学习！"
        
        courses = []
        day_schedule = self.course_schedule.get(weekday, {})
        
        # 检查各个时段的课程
        time_slots = [
            ('morning_1_2', '上午1-2节 (8:00-9:35)'),
            ('morning_3_5', '上午3-5节 (9:45-12:10)'),
            ('afternoon_6_7', '下午6-7节 (14:00-15:35)'),
            ('evening_10_12', '晚上10-12节 (18:30-20:55)')
        ]
        
        for time_slot, time_desc in time_slots:
            if time_slot in day_schedule:
                for course in day_schedule[time_slot]:
                    if self.is_course_in_week(course['weeks'], current_week):
                        courses.append(f"• {time_desc}: {course['name']} ({course['room']})")
        
        if not courses:
            return f"今天第{current_week}周没有课，可以好好休息啦~"
        else:
            return f"今天第{current_week}周有这些课：\n" + "\n".join(courses)
    
    def get_week_schedule(self):
        """获取整周的课程安排"""
        current_week = self.get_current_week()
        
        if current_week == 0:
            return "学期还没开始，好好享受假期吧~"
        
        if current_week > self.total_weeks:
            return "学期已经结束，恭喜你完成了这学期的学习！"
        
        week_days = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        schedule_text = f"第{current_week}周课程安排：\n\n"
        
        for day_num in range(1, 8):
            day_name = week_days[day_num - 1]
            schedule_text += f"{day_name}:\n"
            
            if day_num > 5:  # 周六周日
                schedule_text += "  休息\n\n"
                continue
            
            day_schedule = self.course_schedule.get(day_num, {})
            has_course = False
            
            time_slots = [
                ('morning_1_2', '上午1-2节'),
                ('morning_3_5', '上午3-5节'),
                ('afternoon_6_7', '下午6-7节'),
                ('evening_10_12', '晚上10-12节')
            ]
            
            for time_slot, time_desc in time_slots:
                if time_slot in day_schedule:
                    for course in day_schedule[time_slot]:
                        if self.is_course_in_week(course['weeks'], current_week):
                            schedule_text += f"  {time_desc}: {course['name']} ({course['room']})\n"
                            has_course = True
            
            if not has_course:
                schedule_text += "  休息\n"
            
            schedule_text += "\n"
        
        return schedule_text
    
    def get_course_by_week(self, week_num):
        """获取指定周次的课程安排"""
        if week_num < 1 or week_num > self.total_weeks:
            return f"周次 {week_num} 不在学期范围内 (1-{self.total_weeks}周)"
        
        week_days = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        schedule_text = f"第{week_num}周课程安排：\n\n"
        
        for day_num in range(1, 8):
            day_name = week_days[day_num - 1]
            schedule_text += f"{day_name}:\n"
            
            if day_num > 5:  # 周六周日
                schedule_text += "  休息\n\n"
                continue
            
            day_schedule = self.course_schedule.get(day_num, {})
            has_course = False
            
            time_slots = [
                ('morning_1_2', '上午1-2节'),
                ('morning_3_5', '上午3-5节'),
                ('afternoon_6_7', '下午6-7节'),
                ('evening_10_12', '晚上10-12节')
            ]
            
            for time_slot, time_desc in time_slots:
                if time_slot in day_schedule:
                    for course in day_schedule[time_slot]:
                        if self.is_course_in_week(course['weeks'], week_num):
                            schedule_text += f"  {time_desc}: {course['name']} ({course['room']})\n"
                            has_course = True
            
            if not has_course:
                schedule_text += "  休息\n"
            
            schedule_text += "\n"
        
        return schedule_text
