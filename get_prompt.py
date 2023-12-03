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
            # Find all trials studying a specific disease like Malaria:
            MATCH (t:Trial)-[:TARGETS]->(d:Disease {Name: "Malaria"})
            RETURN t.TrialID, t.Title, t.Phase, t.Status

            # Find all interventions used in a specific trial:
            MATCH (t:Trial {TrialID: "NCT123456"})-[:USES]->(i:Intervention)
            RETURN i.Name, i.Type

            # List all the trials conducted in a specific country:
            MATCH (t:Trial)-[:CONDUCTED_AT]->(l:Location {Country: "India"})
            RETURN t.TrialID, t.Title, t.Status

            # Find all trials and their locations:
            MATCH (t:Trial)-[:CONDUCTED_AT]->(l:Location)
            RETURN t.TrialID, t.Title, l.City, l.Country

            # Find all trials that use a specific type of intervention, like a Drug:
            MATCH (t:Trial)-[:USES]->(i:Intervention {Type: "Drug"})
            RETURN t.TrialID, t.Title, i.Name

 
        The question is:
        {question}
        """
    CYPHER_GENERATION_PROMPT = PromptTemplate(
        input_variables=["schema", "question"], template=CYPHER_GENERATION_TEMPLATE
        )
    return CYPHER_GENERATION_PROMPT
