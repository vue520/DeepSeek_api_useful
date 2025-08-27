from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from openai import OpenAI
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
# 允许跨域请求
CORS(app)

# 初始化OpenAI客户端
client = OpenAI(
    api_key="your _ api",
    base_url="https://api.deepseek.com"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # 获取用户消息
        data = request.get_json()
        user_message = data.get('message', '')
        
        logger.info(f"Received message: {user_message}")
        
        # 调用DeepSeek API
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是我的好朋友，我们相处了很久，你的名字叫何晓彤。"},
                {"role": "user", "content": user_message},
            ],
            stream=False
        )
        
        # 提取AI回复
        ai_response = response.choices[0].message.content
        logger.info(f"AI response: {ai_response}")
        
        return jsonify({
            'success': True,
            'response': ai_response
        })
    
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)