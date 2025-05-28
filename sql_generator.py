# sql_generator.py
import os
from dotenv import load_dotenv
import openai
import httpx

load_dotenv()

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    http_client=httpx.Client(verify=False)
)
def generate_sql(prompt: str, model: str = "gpt-4") -> str:
    """
    Generates a SQL query from a natural language prompt using OpenAI's Chat API.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful SQL assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0,
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Failed to generate SQL: {e}"
