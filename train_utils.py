import os
from langchain.chat_models import AzureChatOpenAI
from langchain.chains import GraphCypherQAChain
from get_prompt import generate_prompt_template
from langchain.graphs import Neo4jGraph
from dotenv import load_dotenv, find_dotenv
from gpt_main import get_gpt_chain
import openai
import json


_ = load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

with open('config.json','r') as file:
    config = json.load(file)

neo4j_config = config['neo4j']
llm_azure_config = config['llm_azure']
streamlit_config = config['streamlit']

graph = Neo4jGraph(**neo4j_config)
graph.refresh_schema()


model = AzureChatOpenAI(**llm_azure_config)
langchain_prompt_template = generate_prompt_template()

gpt_call = get_gpt_chain(model ,graph , langchain_prompt_template)


