import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 流式输出

# 加载.env文件中的环境变量
load_dotenv()

# 创建DeepSeek 聊天模型实例
chat = ChatOpenAI(
    model='deepseek-r1',
    temperature=0,
    api_key=os.getenv("DASHSCOPE_API_KEY"),  # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 定义流式输出
stream = chat.stream([("你是谁！能帮助我解决什么问题？")])
for chunk in stream:
    print(chunk.text(),end='\n')


