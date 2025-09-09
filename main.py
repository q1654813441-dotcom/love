"""
微信定时消息推送主程序
"""
import os
import sys
from dotenv import load_dotenv
from message_scheduler import MessageScheduler

def load_environment():
    """加载环境变量"""
    # 尝试加载.env文件
    if os.path.exists('.env'):
        load_dotenv()
        print("已加载.env文件")
    else:
        print("未找到.env文件，请参考env_example.txt创建配置文件")

def show_menu():
    """显示菜单"""
    print("\n" + "="*50)
    print("💕 微信定时消息推送系统")
    print("="*50)
    print("1. 立即发送测试消息")
    print("2. 启动定时任务")
    print("3. 查看今日课程")
    print("4. 查看本周课程")
    print("5. 查看指定周次课程")
    print("6. 查看恋爱天数")
    print("7. 查看大姨妈信息")
    print("8. 查看天气信息")
    print("9. 查看星座运势")
    print("0. 退出程序")
    print("="*50)

def main():
    """主函数"""
    print("正在初始化系统...")
    
    # 加载环境变量
    load_environment()
    
    # 创建消息调度器
    scheduler = MessageScheduler()
    
    while True:
        show_menu()
        choice = input("请选择操作 (0-9): ").strip()
        
        if choice == '1':
            print("\n正在发送测试消息...")
            scheduler.test_message()
            
        elif choice == '2':
            print("\n启动定时任务...")
            scheduler.start_scheduler()
            
        elif choice == '3':
            print("\n今日课程安排：")
            courses = scheduler.schedule_manager.get_today_courses()
            print(courses)
            
        elif choice == '4':
            print("\n本周课程安排：")
            week_schedule = scheduler.schedule_manager.get_week_schedule()
            print(week_schedule)
            
        elif choice == '5':
            try:
                week_num = int(input("请输入要查看的周次 (1-20): "))
                print(f"\n第{week_num}周课程安排：")
                course_schedule = scheduler.schedule_manager.get_course_by_week(week_num)
                print(course_schedule)
            except ValueError:
                print("请输入有效的周次数字！")
            
        elif choice == '6':
            print("\n恋爱信息：")
            love_info = scheduler.love_calculator.get_love_info()
            print(love_info)
            
        elif choice == '7':
            print("\n大姨妈信息：")
            period_info = scheduler.period_tracker.get_period_info()
            print(period_info)
            
        elif choice == '8':
            print("\n天气信息：")
            weather_data = scheduler.weather_api.get_current_weather()
            print(f"温度: {weather_data['temperature']}")
            print(f"体感温度: {weather_data['feels_like']}")
            print(f"天气: {weather_data['description']}")
            print(f"湿度: {weather_data['humidity']}")
            print(f"风速: {weather_data['wind']}")
            
        elif choice == '9':
            print("\n星座运势：")
            fortune_data = scheduler.constellation_api.get_daily_fortune()
            constellation_info = scheduler.constellation_api.format_fortune_message(fortune_data)
            print(constellation_info)
            
        elif choice == '0':
            print("\n感谢使用，再见！")
            break
            
        else:
            print("\n无效选择，请重新输入！")
        
        input("\n按回车键继续...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n程序被用户中断")
        sys.exit(0)
    except Exception as e:
        print(f"\n程序运行出错: {e}")
        sys.exit(1)
