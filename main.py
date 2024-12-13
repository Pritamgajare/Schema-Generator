import streamlit as st
from chains import SQLSchemaGenerator

def create_streamlit_app(sql_generator):
    st.title("🛠️ SQL Schema Generator")
    st.markdown("Generate SQL schemas based on your custom requirements!")

    user_input = st.text_area(
        "Enter your prompt for the SQL schema:",
        placeholder="E.g., Create a schema for a library system with books, authors, and borrowers."
    )

    generate_button = st.button("Generate SQL Schema")

    if generate_button:
        if user_input.strip():
            with st.spinner("Generating SQL Schema... Please wait."):
                try:
                    schema = sql_generator.generate_schema(user_input)
                    st.code(schema, language="sql")

                    if st.button("Copy to Clipboard"):
                        st.session_state.generated_schema = schema
                        st.success("Schema copied to clipboard!")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a valid prompt.")

if __name__ == "__main__":
    sql_generator = SQLSchemaGenerator()
    st.set_page_config(layout="wide", page_title="SQL Schema Generator", page_icon="🛠️")
    create_streamlit_app(sql_generator)
