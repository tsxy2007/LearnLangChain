import langchain
from langchain_deepseek import ChatDeepSeek
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

# 加载.env文件中的环境变量
load_dotenv()
model = init_chat_model("deepseek-reasoner",model_provider="deepseek")

from langchain_core.prompts import ChatPromptTemplate

system_template = "识别语言,并把该语言翻译到 {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

prompt = prompt_template.invoke({"language": "Chinese", "text": "hello world"})

print(prompt)

print(prompt.to_messages())

response = model.invoke(prompt)
print(response.content)