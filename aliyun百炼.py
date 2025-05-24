import os
from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chat_models import init_chat_model



# 加载.env文件中的环境变量
load_dotenv()

# 创建DeepSeek 聊天模型实例
chat = ChatOpenAI(
    model='deepseek-r1',
    temperature=0,
    api_key=os.getenv("DASHSCOPE_API_KEY"),  # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 定义对话消息列表,包含系统角色消息和用户消息角色
messages = [
                (
                    "system",
                    "You are a helpful translator. Translate the user sentence to Chinese.",
                ),
                ("human", "I love programming."),
            ]
response = chat.invoke(messages)
print(response.content)