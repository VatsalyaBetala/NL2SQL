# app.py
import streamlit as st
from schema_loader import load_schema_from_file
from prompt_generation import build_prompt
from sql_generator import generate_sql

SCHEMA_PATH = r"C:\Users\VatsalyaBetala\Documents\NL2SQL\data\DDL.sql"
schema = load_schema_from_file(SCHEMA_PATH)

st.set_page_config(page_title="AI SQL Assistant", layout="wide")
st.title("NL2SQL")
with st.sidebar:
    st.header("⚙️ Settings")
    model = st.selectbox("Choose model", ["gpt-3.5-turbo", "gpt-4"], index=1)
    show_schema = st.checkbox("🔍 Show schema")
    auto_run = st.checkbox("⚡ Auto-run SQL after generation")

question = st.text_area("Enter your natural language question", height=120)

if st.button("Generate SQL"):
    with st.spinner("Generating SQL..."):
        prompt = build_prompt(schema, question)
        sql_query = generate_sql(prompt, model=model)

        st.code(sql_query, language='sql')

        if "drop" in sql_query.lower() or "delete" in sql_query.lower():
            st.warning("⚠️ This query contains destructive keywords.")

        # Optional future feature: run query here
        if auto_run:
            st.info("🛠 SQL execution feature coming soon!")

if show_schema:
    with st.expander("📘 Schema"):
        st.code(schema, language="sql")
