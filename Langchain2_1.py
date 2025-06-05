import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

# 提示词模板

prompt_template = ChatPromptTemplate.from_messages([
    ("system","把下面的文字翻译成{语言}"),
    ("user","{内容}")
])

# 构建阿里云百炼大模型客户端
llm = ChatOpenAI(
    model="qwen-plus",
    api_key=os.getenv("DASHSCOPE_API_KEY"),  # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 结果解析器 stroutputParser 会AIMessage转换成str，实际上就是获取AIMessage的content属性
parser = StrOutputParser()

# 构建链
chain = prompt_template | llm | parser

# 直接调用链

print(chain.invoke({"内容":"nice to meet you", "语言":"中文"}))

# 继续添加新链条

analysis_prompt = ChatPromptTemplate.from_template("我应该怎么回答这个问题？{talk}.给我一个五字以内的示例")

chain2 = {"talk":chain} | analysis_prompt | llm | parser

print(chain2.invoke({"内容":"nice to meet you", "语言":"中文"}))