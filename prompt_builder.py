def build_prompt(schema_text: str, user_question: str) -> str:
    """
    Creates a prompt for the LLM by combining schema and user input.
    """
    prompt = f"""

    You are a SQL expert assistant.
    Here is the database schema:

    {schema_text}

    Translate the following natural language question into a SQL query:

    Question: "{user_question}"

    Only generate the SQL query. Do not explain or comment. Keep in mind these two thing, while acessing the tables you have to mention gtp.dbo.(table name)
    
    """
    
    return prompt

if __name__ == "__main__":

    from schema_loader import load_schema_from_file
    
    schema = load_schema_from_file(r"C:\Users\VatsalyaBetala\Documents\NL2SQL\static_gtp_schema.sql")
    user_question = "List the total quantity of each SKU available in the warehouse."
    
    prompt = build_prompt(schema, user_question)
    print(prompt[:1000])  # preview
