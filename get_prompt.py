from langchain.prompts.prompt import PromptTemplate
 
 
def generate_prompt_template():
    """
    Returns a Langchain prompt template
    """
    CYPHER_GENERATION_TEMPLATE =  """
            You are an assistant whose task is to Generate Cypher statement to query a graph database and return results in human readable format which will in turn be used by medical profeesionals to read clinical trials

            Instructions:
            - Use only the provided relationship types and properties in the schema.
            - Do not use any other relationship types or properties that are not provided.
            - The values stored in graph database are in lowercase , so convert the query in lowercase before processing.
            Schema (Nodes, Relationships, Properties):
            {schema}

            The question is:
            {question}
        """
    CYPHER_GENERATION_PROMPT = PromptTemplate(
        input_variables=["schema", "question"], template=CYPHER_GENERATION_TEMPLATE
        )
    return CYPHER_GENERATION_PROMPT
