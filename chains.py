import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class SQLSchemaGenerator:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

    def generate_schema(self, user_prompt):
        prompt_schema = PromptTemplate.from_template(
            """
            ### USER PROMPT:
            {prompt}
            ### INSTRUCTION:
            Based on the given user prompt, generate SQL schemas for the described requirements. Ensure the schema includes 
            appropriate table names, columns, data types, primary keys, and foreign keys where applicable. Return only the 
            valid SQL script.
            ### SQL SCHEMA (NO PREAMBLE):
            """
        )
        chain_schema = prompt_schema | self.llm
        res = chain_schema.invoke(input={"prompt": user_prompt})
        try:
            return res.content
        except Exception as e:
            raise OutputParserException(f"Error generating schema: {e}")

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))
