#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
微信定时消息推送系统启动脚本
适用于宝塔面板部署
"""

import os
import sys
import logging
from datetime import datetime
from message_scheduler import MessageScheduler

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('wechat_message.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def main():
    """主函数"""
    logging.info("="*60)
    logging.info("💕 微信定时消息推送系统启动中...")
    logging.info("="*60)
    
    try:
        # 创建消息调度器
        scheduler = MessageScheduler()
        logging.info("✅ 消息调度器创建成功")
        
        # 测试一次消息发送
        logging.info("🧪 发送测试消息...")
        scheduler.test_message()
        
        logging.info("✅ 系统启动成功！")
        logging.info("⏰ 定时任务已启动，每天定时发送消息")
        logging.info("按 Ctrl+C 停止程序")
        logging.info("="*60)
        
        # 启动定时任务
        scheduler.start_scheduler()
        
    except KeyboardInterrupt:
        logging.info("\n🛑 程序被用户中断")
        sys.exit(0)
    except Exception as e:
        logging.error(f"❌ 程序运行出错: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
