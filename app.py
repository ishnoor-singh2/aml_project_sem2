import streamlit as st
import os
from langchain.chat_models import AzureChatOpenAI
from langchain.chains import GraphCypherQAChain
from get_prompt import generate_prompt_template
from langchain.graphs import Neo4jGraph
from dotenv import load_dotenv, find_dotenv
from gpt_main import get_gpt_chain
import openai
import json
import time
from streamlit_option_menu import option_menu
from streamlit_chat import message


_ = load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

with open('config.json','r') as file:
    config = json.load(file)

neo4j_config = config['neo4j']
llm_azure_config = config['llm_azure']
streamlit_config = config['streamlit']



st.set_page_config(
    page_title="Natural Language Interface to Knoledge graph",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)



#Creating the chatbot interface
st.title("Natural Language Interface to Clinical Trial data")

with st.sidebar:
    selected = option_menu("Main Menu", ["ABOUT", "Upload Data", "Model Interface", 'SETTINGS'], 
        icons=['house','1-circle','2-circle' ,'gear'], menu_icon="cast", default_index=0)
    
    if selected == "ABOUT":
        st.sidebar.markdown(
        """
        ## Example questions

        * List the trial id of trial studing Hematologic Malignancy disease and give it's url?
        * List the titles of the trials in China?
        * I have a patient having Borderline Personality Disorder , 
          suggest some trial studying Borderline Personality Disorder, give me it's brief summary in a line?
        * List the title of all trials in happening in Switzerland.?
        * Show the top trial based on studyStartDate studying Overweight and Obesity give the trial's url?
        * I have a patient having Parkinson´s Disease , suggest some trial studying Parkinson´s Disease?
        * Explain in  short about the trial studying Arrythmia and give it's URL?

        NOTE: Currently the app is under develeopement , the responses and data might not be accurate
        """
        ) 


if "user_input" not in st.session_state:
    st.session_state["user_input"] = []
if "model_response" not in st.session_state:
    st.session_state["model_response"] = []



query = st.text_input("")

if query:
    with st.spinner(text='In progress'):
        time.sleep(3)
        try:
            graph = Neo4jGraph(**neo4j_config)
            graph.refresh_schema()
            model = AzureChatOpenAI(**llm_azure_config)
            langchain_prompt_template = generate_prompt_template()
            gpt_call = get_gpt_chain(model ,graph , langchain_prompt_template)
            return_val = gpt_call.run(query)
            st.session_state["user_input"].append(query)
            st.session_state["model_response"].append(return_val)
            st.success('Done')
        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.write("Please write a query in natural language 🩺")

# Display chat history
for i in range(len(st.session_state["user_input"])):
    with st.container():
        with st.chat_message("user"):
            st.write(st.session_state["user_input"][i])
        with st.chat_message("assistant"):
            st.write(st.session_state["model_response"][i])