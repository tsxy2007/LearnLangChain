import langchain
from langchain_deepseek import ChatDeepSeek
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

# 加载.env文件中的环境变量
load_dotenv()

# 创建DeepSeek 聊天模型实例
chat = ChatDeepSeek(
    temperature=0,
    model='deepseek-reasoner',
    api_key=os.getenv("DEEPSEEK_API_KEY")
)

# 定义对话消息列表,包含系统角色消息和用户消息角色
messages = [
    {'role':'system','content':'你是一个有帮助的AI助手。'},
    {'role':'user','content':'你好！请介绍下自己。'}
]

response = chat.invoke(messages)
print(response.content)
print(langchain.__version__)

