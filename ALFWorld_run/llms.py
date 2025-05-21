import os
import tiktoken
token_enc = tiktoken.get_encoding("cl100k_base")

from dotenv import load_dotenv

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)

load_dotenv()

OPENAI_CHAT_MODELS = ["gpt-3.5-turbo","gpt-3.5-turbo-16k-0613","gpt-3.5-turbo-16k","gpt-4-0613","gpt-4-32k-0613", "gpt-4o", "gpt-4"]
FASTCHAT_MODELS = ["llama-2-13b-chat","vicuna-7b"]
DEEPSEEK_MODELS = ["deepseek-chat"]
KIMI_MODELS = ["moonshot-v1-8k"]
LOCAL_HUGGINGFACE_MODELS = ["",]


class langchain_deepseek_llm:
    def __init__(self, llm_name, temperature=0.7, max_tokens=128):
        from langchain_community.chat_models import ChatOpenAI
        # model
        chat = ChatOpenAI(
            model=llm_name,
            temperature=temperature, 
            # max_tokens=max_tokens,
            api_key=os.getenv("DEEPSEEK_API_KEY", None),
            base_url=os.getenv("DEEPSEEK_BASE_URL", None),
        )
        # prompt
        user_message_prompt = HumanMessagePromptTemplate.from_template("{input}")
        chat_prompt = ChatPromptTemplate.from_messages([user_message_prompt])
        # output format
        output_parser = StrOutputParser()

        self.chain = chat_prompt | chat | output_parser
   
    def run(self, prompt, temperature=1, max_tokens=128):
        # run api
        return self.chain.invoke(
                prompt, 
                temperature=temperature, 
                # max_tokens=max_tokens
            )


class langchain_kimi_chatllm:
    def __init__(self, llm_name, temperature=0.7, max_tokens=128):
        from langchain_community.chat_models import ChatOpenAI
        # model
        chat = ChatOpenAI(
            model=llm_name,
            temperature=temperature, 
            max_tokens=max_tokens,

            api_key=os.getenv("KIMI_API_KEY", None),
            base_url=os.getenv("KIMI_BASE_URL", None),
        )
        # prompt
        user_message_prompt = HumanMessagePromptTemplate.from_template("{input}")
        chat_prompt = ChatPromptTemplate.from_messages([user_message_prompt])
        # output format
        output_parser = StrOutputParser()

        self.chain = chat_prompt | chat | output_parser
   
    def run(self, prompt, temperature=1, max_tokens=128):
        # run api
        return self.chain.invoke(
                prompt, 
                temperature=temperature, 
                max_tokens=max_tokens
            )


class langchain_openai_chatllm:
    def __init__(self, llm_name, temperature=0.7, max_tokens=128):
        from langchain_openai.chat_models import ChatOpenAI
        import openai
        openai.api_key = os.getenv("OPENAI_API_KEY", None)
        openai.api_base = os.getenv("OPENAI_BASE_URL_CN", None)
        # model
        chat = ChatOpenAI(
            model=llm_name,
            temperature=temperature, 
            # max_tokens=max_tokens,

            api_key=os.getenv("OPENAI_API_KEY", None),
            base_url=os.getenv("OPENAI_BASE_URL_CN", None),
        )
        # prompt
        user_message_prompt = HumanMessagePromptTemplate.from_template("{input}")
        chat_prompt = ChatPromptTemplate.from_messages([user_message_prompt])
        # output format
        output_parser = StrOutputParser()

        self.chain = chat_prompt | chat | output_parser
   
    def run(self, prompt, temperature=0.7, max_tokens=128):
        # run api
        return self.chain.invoke(
                prompt, 
                temperature=temperature, 
                # max_tokens=max_tokens
            )


class langchain_huggingface_llm:
    def __init__(self, model_id, temperature=0.7, max_tokens=128):
        from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
        # prepare huggingface model
        pipe = HuggingFacePipeline.from_model_id(
            model_id=model_id,
            task="text-generation",
            pipeline_kwargs=dict(
                max_new_tokens=max_tokens,
                temperature=temperature,
                do_sample=False,
                repetition_penalty=1.03,
            )
        )
        # model
        chat = ChatHuggingFace(llm=pipe,)
        # prompt
        user_message_prompt = HumanMessagePromptTemplate.from_template("{input}")
        chat_prompt = ChatPromptTemplate.from_messages([user_message_prompt])
        # output format
        output_parser = StrOutputParser()

        self.chain = chat_prompt | chat | output_parser
    
    def run(self, prompt, temperature=0.9, stop=['\n'], max_tokens=128):
        # run api
        return self.chain.invoke(
                prompt, 
                temperature=temperature, 
                max_tokens=max_tokens,
                stop = stop,
        )
def get_llm_backend(llm_name, **kwargs):
    if llm_name in OPENAI_CHAT_MODELS:
        return langchain_openai_chatllm(llm_name, **kwargs)
    elif llm_name in DEEPSEEK_MODELS:
        return langchain_deepseek_llm(llm_name, **kwargs)
    elif llm_name in KIMI_MODELS:
        return langchain_kimi_chatllm(llm_name, **kwargs)
    else:
        return langchain_huggingface_llm(llm_name, **kwargs)