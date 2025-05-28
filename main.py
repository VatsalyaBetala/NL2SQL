from schema_loader import load_schema_from_file
from prompt_generation import build_prompt
from sql_generator import generate_sql

schema = load_schema_from_file(r"C:\Users\VatsalyaBetala\Documents\NL2SQL\data\DDL.sql")

while True:

    question = str(input("Enter your question: "))
    
    # Terminating Loop
    if question == "exit" or question == "exit()": 
        print("Thanks for using NL2SQL")
        break
    
    prompt = build_prompt(schema, question)
    sql_query = generate_sql(prompt)

    print("SQL Generated:\n", sql_query)
