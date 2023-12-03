from langchain.prompts.prompt import PromptTemplate
 
 
def generate_prompt_template():
    """
    Returns a Langchain prompt template
    """
    CYPHER_GENERATION_TEMPLATE =  """
        You are an assistant whose task is to Generate Cypher statement to query a graph database and return results in human readable format which will in turn be used by medical profeesionals to read clinical trials
 
        Instructions:
        - Use only the information stored in the graph.Do not use any external information in your answer.
        - Use only the provided relationship types and properties in the schema.
        - The answer should only Include only the provided information from the query.Nothing else should be included.
 
        Schema (Nodes, Relationships, Properties):
        {schema}
 
        Examples:
        # Find all trials studying a specific disease like Covid-19:
        MATCH (t:Trial)-[:STUDIES]->(d:Disease {{diseaseName: "Covid-19"}})
        RETURN t.title, t.phase, t.status
 
        # Find all drugs used in a specific trial:
        MATCH (t:Trial {{trialID: "CT123456"}})-[:USES]->(d:Drug)
        RETURN d.drugName, d.dosage, d.modeOfAdministration
 
        # Find all trials sponsored by a specific sponsor:
        MATCH (t:Trial)-[:SPONSORED_BY]->(s:Sponsor {{sponsorName: "Sponsor Name Here"}})
        RETURN t.title, t.phase, t.status
 
        The question is:
        {question}
        """
    CYPHER_GENERATION_PROMPT = PromptTemplate(
        input_variables=["schema", "question"], template=CYPHER_GENERATION_TEMPLATE
        )
    return CYPHER_GENERATION_PROMPT
