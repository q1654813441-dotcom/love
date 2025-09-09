module.exports = {
  apps: [{
    name: 'wechat-message',
    script: 'start.py',
    interpreter: 'python3',
    cwd: '/www/wwwroot/wechat-message',
    instances: 1,
    autorestart: true,
    watch: false,
    max_memory_restart: '1G',
    env: {
      NODE_ENV: 'production'
    },
    error_file: './logs/err.log',
    out_file: './logs/out.log',
    log_file: './logs/combined.log',
    time: true
  }]
}
