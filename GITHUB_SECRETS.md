# GitHub Secrets 配置说明

## 环境变量设置

在GitHub仓库中设置以下Secrets，路径：`Settings` → `Secrets and variables` → `Actions` → `New repository secret`

### 微信测试号配置

| 变量名 | 值 | 说明 |
|--------|----|----|
| `WECHAT_APP_ID` | `wx4bce032616c5d598` | 微信测试号AppID |
| `WECHAT_APP_SECRET` | `65201a5d86e8292350850ea51960040e` | 微信测试号AppSecret |
| `WECHAT_TEMPLATE_ID` | `wC6BYEM-wNW5Agumfqm1_XQyEfAfM9orHh7AyloHt7k` | 微信模板ID |
| `WECHAT_USER_OPENID` | `oEBD511jdtj1vPOjffxvHbYliEmM` | 接收消息的OpenID |

### 天气API配置

| 变量名 | 值 | 说明 |
|--------|----|----|
| `WEATHER_API_KEY` | `a8535e8e97b46147ad50fba96ae9c523` | 聚合数据天气API密钥 |
| `WEATHER_KEY_ID` | `TC5BTDMYMP` | 和风天气凭据ID（备用） |
| `WEATHER_CITY` | `福州` | 城市名称 |

### 个人信息配置

| 变量名 | 值 | 说明 |
|--------|----|----|
| `CONSTELLATION` | `狮子座` | 女朋友的星座 |
| `LOVE_START_DATE` | `2025-05-16` | 恋爱开始日期 (YYYY-MM-DD) |
| `GIRLFRIEND_BIRTHDAY` | `2006-07-26` | 女朋友生日 (YYYY-MM-DD) |

### 大姨妈配置

| 变量名 | 值 | 说明 |
|--------|----|----|
| `PERIOD_CYCLE_DAYS` | `30` | 月经周期天数 |
| `PERIOD_LAST_DATE` | `2024-12-23` | 上次月经开始日期 (YYYY-MM-DD) |
| `PERIOD_DAYS` | `5` | 月经持续天数 |

### 学期配置

| 变量名 | 值 | 说明 |
|--------|----|----|
| `SEMESTER_START_DATE` | `2025-09-01` | 学期开始日期 (YYYY-MM-DD) |
| `SEMESTER_TOTAL_WEEKS` | `20` | 学期总周数 |

### 推送时间配置

| 变量名 | 值 | 说明 |
|--------|----|----|
| `PUSH_TIME` | `08:00` | 每天推送时间 |

## 配置步骤

1. **进入仓库设置**
   - 在GitHub仓库页面点击 `Settings`

2. **添加Secrets**
   - 左侧菜单选择 `Secrets and variables` → `Actions`
   - 点击 `New repository secret`
   - 输入变量名和对应的值
   - 点击 `Add secret`

3. **重复添加**
   - 重复上述步骤，添加所有必需的环境变量

4. **验证配置**
   - 所有Secrets添加完成后，GitHub Actions将自动每天北京时间8点运行
   - 也可以在 `Actions` 页面手动触发运行

## 注意事项

- ⚠️ **不要在代码中直接写入敏感信息**
- ✅ 所有敏感配置都通过GitHub Secrets管理
- 🔒 Secrets一旦设置，无法查看，只能重新设置
- 📅 默认每天北京时间8点自动运行
- 🔧 可以在Actions页面查看运行日志和状态

## 时区说明

- GitHub Actions使用UTC时间
- 配置的 `cron: '0 0 * * *'` 表示UTC 0点
- 对应北京时间上午8点（UTC+8）
- 如需修改时间，请调整 `.github/workflows/daily-message.yml` 中的cron表达式
