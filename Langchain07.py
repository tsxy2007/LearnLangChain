import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableMap,RunnableLambda


# 定制参数

# 加载.env文件中的环境变量
load_dotenv()

# 提示词模板
from langchain_core.prompts import ChatPromptTemplate
prompt_template_zh = ChatPromptTemplate.from_messages(
    [
        ('system','Translate the following from Enginsh into chinese'),
        ('user','{text}')
    ]
)

prompt_template_fr = ChatPromptTemplate.from_messages(
    [
        ('system','Translate the following from Enginsh into French'),
        ('user','{text}')
    ]
)

# 创建DeepSeek 聊天模型实例
llm = ChatOpenAI(
    model='deepseek-r1',
    temperature=0,
    api_key=os.getenv("DASHSCOPE_API_KEY"),  # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 结果解析器 strOutParse 会AIMessage转换成str,实际上就是i获取AIMessage的Content属性
from langchain_core.output_parsers import StrOutputParser
parse = StrOutputParser()

# 构建链
chain_zh = prompt_template_zh | llm | parse
chain_fr = prompt_template_fr | llm | parse


# 并行处理
parallel_chains = RunnableMap({
    'zh_translation':chain_zh,
    "fr_translation":chain_fr
})

# 合并结果
final_chain = parallel_chains | RunnableLambda(lambda x:f"Chinese:{x['zh_translation']}\nFrench:{x['fr_translation']}")
print(final_chain.invoke({'text':'nice to meet you'}))

final_chain.get_graph().print_ascii()