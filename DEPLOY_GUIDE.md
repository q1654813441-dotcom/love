# 🚀 GitHub Actions 部署指南

## 快速部署步骤

### 1. Fork 仓库
1. 点击本仓库右上角的 `Fork` 按钮
2. 将仓库fork到你的GitHub账号下

### 2. 配置 GitHub Secrets
在你的仓库中设置以下环境变量：

1. 进入你fork的仓库
2. 点击 `Settings` 选项卡
3. 左侧菜单选择 `Secrets and variables` → `Actions`
4. 点击 `New repository secret` 添加以下变量：

#### 必需配置
```
WECHAT_APP_ID=wx4bce032616c5d598
WECHAT_APP_SECRET=65201a5d86e8292350850ea51960040e
WECHAT_TEMPLATE_ID=wC6BYEM-wNW5Agumfqm1_XQyEfAfM9orHh7AyloHt7k
WECHAT_USER_OPENID=oEBD511jdtj1vPOjffxvHbYliEmM
WEATHER_API_KEY=a8535e8e97b46147ad50fba96ae9c523
WEATHER_CITY=福州
CONSTELLATION=狮子座
LOVE_START_DATE=2025-05-16
GIRLFRIEND_BIRTHDAY=2006-07-26
PERIOD_CYCLE_DAYS=30
PERIOD_LAST_DATE=2024-12-23
PERIOD_DAYS=5
SEMESTER_START_DATE=2025-09-01
SEMESTER_TOTAL_WEEKS=20
PUSH_TIME=08:00
```

#### 可选配置
```
WEATHER_KEY_ID=TC5BTDMYMP
```

### 3. 启用 GitHub Actions
1. 在你的仓库中点击 `Actions` 选项卡
2. 如果提示启用工作流，点击 `I understand my workflows, go ahead and enable them`

### 4. 测试运行
1. 在 `Actions` 页面，点击左侧的 `每日微信消息推送` 工作流
2. 点击右侧的 `Run workflow` 按钮进行手动测试
3. 查看运行日志，确认消息发送成功

### 5. 自动运行
- 系统将在每天北京时间上午8点自动运行
- 你也可以随时手动触发运行

## ⚠️ 注意事项

1. **时区设置**：默认北京时间8点推送，如需修改请编辑 `.github/workflows/daily-message.yml`
2. **Secrets安全**：不要在代码中直接写入敏感信息，都通过Secrets配置
3. **运行频率**：免费GitHub账户每月有2000分钟的Actions运行时间
4. **日志查看**：可在Actions页面查看每次运行的详细日志

## 🔧 自定义配置

### 修改推送时间
编辑 `.github/workflows/daily-message.yml` 中的 cron 表达式：
```yaml
schedule:
  - cron: '0 0 * * *'  # UTC 0点 = 北京时间8点
```

### 修改推送频率
可以设置为每周、每月等，cron表达式参考：
- `0 0 * * 1-5`：工作日推送
- `0 0 * * 1,3,5`：周一、三、五推送

## 🐛 故障排除

### 消息发送失败
1. 检查微信测试号配置是否正确
2. 确认模板ID和OpenID有效
3. 查看Actions运行日志获取详细错误信息

### Actions运行失败
1. 检查所有必需的Secrets是否都已配置
2. 确认Secrets的值没有多余的空格
3. 查看运行日志中的具体错误信息

### 获取不到天气信息
1. 检查聚合数据API密钥是否有效
2. 确认城市名称正确
3. 系统有备用天气信息，不会影响消息发送

## ✅ 验证部署成功

部署成功后，你应该能看到：
1. Actions页面显示绿色的成功状态
2. 微信收到测试消息
3. 每天定时收到消息推送

**🎉 恭喜！你的微信定时消息推送系统已成功部署到GitHub！**
