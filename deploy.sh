#!/bin/bash

# 微信定时消息推送系统部署脚本
# 适用于宝塔面板

echo "🚀 开始部署微信定时消息推送系统..."

# 创建日志目录
mkdir -p logs

# 安装依赖
echo "📦 安装Python依赖..."
pip install -r requirements.txt

# 检查配置文件
if [ ! -f "config.py" ]; then
    echo "⚠️  配置文件不存在，请复制 config_backend.py 为 config.py 并填入配置信息"
    cp config_backend.py config.py
    echo "✅ 已创建配置文件模板，请编辑 config.py 文件"
fi

# 设置权限
chmod +x start.py

echo "✅ 部署完成！"
echo "📝 请按照 宝塔部署说明.md 完成后续配置"
echo "🔧 配置文件：config.py"
echo "🚀 启动脚本：start.py"
