from langchain.chat_models import AzureChatOpenAI
from langchain.chains import GraphCypherQAChain
 
 
def get_gpt_chain(model , graph,langchain_prompt_template,verbose=True, return_direct=True):
    return GraphCypherQAChain.from_llm(
        model, graph=graph, verbose=verbose, cypher_prompt=langchain_prompt_template,validate_cypher=True
    )