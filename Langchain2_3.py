import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

# 构建阿里云百炼大模型客户端
llm = ChatOpenAI(
    model="qwen-plus",
    api_key=os.getenv("DASHSCOPE_API_KEY"),  # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

from langchain_redis import RedisChatMessageHistory
history = RedisChatMessageHistory(
                session_id="my-redis",
                redis_url="redis://localhost:6379",
                ttl=3600  # Expire chat history after 1 hour
            )

from langchain_core.runnables.history import RunnableWithMessageHistory

runnable = RunnableWithMessageHistory(
    llm,
    get_session_history=lambda: history,
)

result = runnable.invoke({"text":"请重复一次"})

print(result.content)