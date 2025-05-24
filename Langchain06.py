import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


# 定制参数

# 加载.env文件中的环境变量
load_dotenv()

# 提示词模板
from langchain_core.prompts import ChatPromptTemplate
prompt_template = ChatPromptTemplate.from_messages(
    [
        ('system','Translate the following from Enginsh into {language}'),
        ('user','{text}')
    ]
)


# 创建DeepSeek 聊天模型实例
chat = ChatOpenAI(
    model='deepseek-r1',
    temperature=0.5,
    api_key=os.getenv("DASHSCOPE_API_KEY"),  # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 结果解析器 strOutParse 会AIMessage转换成str,实际上就是i获取AIMessage的Content属性
from langchain_core.output_parsers import StrOutputParser
parse = StrOutputParser()

# 构建链
chain = prompt_template | chat | parse

# 直接使用链
# print(chain.invoke({'text':'nice to meet you','language':'chinese'}))


# 构建回复模板
analysis_prompt = ChatPromptTemplate.from_template("我应该怎么回答这句话？{talk}。")
# 构建链2
chain2 = {"talk":chain} | analysis_prompt | chat | parse

print(chain2.invoke({'text':'nice to meet you','language':'chinese'}))
