🤖 DeepSeek聊天助手项目

一个基于Flask和DeepSeek API的智能聊天助手Web应用，具有美观的UI界面和流畅的对话体验。

✨ 功能特性

· 🎨 现代化美观的聊天界面
· 🤖 集成DeepSeek AI大语言模型
· 💬 实时对话交互
· 📱 响应式设计，支持移动端
· 🔄 自动滚动到底部
· 🌐 跨域请求支持(CORS)
· 🏥 健康检查端点

🛠️ 技术栈

· 后端: Python + Flask
· 前端: HTML5 + CSS3 + JavaScript
· AI服务: DeepSeek API
· 网络: Flask-CORS

📦 项目结构

```
deepseek-chat-assistant/
├── app.py                 # Flask后端主程序
├── requirements.txt       # Python依赖包
└── templates/
    └── index.html        # 前端页面
```

🚀 快速开始

1. 环境要求

· Python 3.7+
· pip (Python包管理器)

2. 安装依赖

```bash
# 克隆项目
git clone <your-repo-url>
cd deepseek-chat-assistant

# 创建虚拟环境（可选但推荐）
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt
```

3. 配置API密钥

在app.py中替换您的DeepSeek API密钥：

```python
client = OpenAI(
    api_key="your-deepseek-api-key-here",  # 替换为您的实际密钥
    base_url="https://api.deepseek.com"
)
```

4. 运行应用

```bash
python app.py
```

应用将在 http://127.0.0.1:5000 启动

📝 API端点

聊天接口

· URL: /chat
· 方法: POST
· 参数:
  ```json
  {
    "message": "用户输入的消息"
  }
  ```
· 响应:
  ```json
  {
    "success": true,
    "response": "AI回复内容"
  }
  ```

健康检查

· URL: /health
· 方法: GET
· 响应:
  ```json
  {
    "status": "healthy"
  }
  ```

⚙️ 配置说明

修改端口

在app.py末尾修改端口号：

```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # 修改端口号
```

自定义AI角色

在app.py中修改系统提示：

```python
messages=[
    {"role": "system", "content": "自定义角色描述"},
    {"role": "user", "content": user_message},
]
```

🔧 故障排除

常见问题

1. 端口被占用
   ```bash
   # 查找占用端口的进程
   lsof -i :5000
   # 或
   netstat -ano | findstr :5000
   ```
2. API密钥错误
   · 检查DeepSeek API密钥是否正确
   · 确认账户余额充足
3. 跨域问题
   · 确保Flask-CORS已正确安装和配置

日志查看

应用运行时会在控制台输出详细日志，包括请求和错误信息。

🌐 部署建议

生产环境部署

```bash
# 使用Gunicorn（推荐）
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# 或使用Waitress
pip install waitress
waitress-serve --port=5000 app:app
```

Docker部署

创建Dockerfile：

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

构建并运行：

```bash
docker build -t deepseek-chat .
docker run -p 5000:5000 deepseek-chat
```

📄 许可证

本项目仅供学习和研究使用，请遵守DeepSeek API的使用条款。

🤝 贡献

欢迎提交Issue和Pull Request来改进这个项目！

📞 支持

如有问题，请通过以下方式联系：

· 创建GitHub Issue
· 发送邮件至: wangchunhao479@outlook.com

---

注意: 请确保遵守相关API服务的使用条款和法律法规。

