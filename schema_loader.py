from pathlib import Path
def load_schema_from_file(path:str) -> str:
    """
    Loads a static schema file and returns it's content as a string
    This could be passed to the LLM for query generation.
    """ 
    schema_file = Path(path)
    
    if not schema_file.exists():
        raise FileNotFoundError(f"Schema file not found at {path}")
    
    return schema_file.read_text(encoding='utf-8')

if __name__ == "__main__": 
    schema_path = r"C:\Users\VatsalyaBetala\Documents\NL2SQL\data\static_gtp_schema.sql"
    text = load_schema_from_file(schema_path)
    print(text[:100]) 