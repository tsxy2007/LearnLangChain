import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 提示词模板

# 加载.env文件中的环境变量
load_dotenv()

# 创建DeepSeek 聊天模型实例
chat = ChatOpenAI(
    model='deepseek-r1',
    temperature=0,
    api_key=os.getenv("DASHSCOPE_API_KEY"),  # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


# 提示词
from langchain_core.prompts import ChatPromptTemplate

promt_template = ChatPromptTemplate.from_messages(
    [
        ("system","将{language}翻译成中文"),
        ("user","{Text}")
    ]
)

prompt = promt_template.invoke({"language":"English","Text":"Hello, how are you"});
# print(prompt)

response = chat.invoke(prompt)
print(response.content)