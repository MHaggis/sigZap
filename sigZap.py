import streamlit as st
import sqlite3
import pandas as pd
import re

st.set_page_config(page_title="sigZap", layout="wide")

conn = sqlite3.connect('rules.db')
query = "SELECT * FROM rule_sets"
df = pd.read_sql_query(query, conn)
conn.close()

st.title('sigZap')
st.markdown("""
    This is a Streamlit application designed to facilitate the search across multiple network signature sets at once. 
    It provides a user-friendly interface to quickly and efficiently query different rule sets. 
    The application connects to a SQLite database where the rule sets are stored and allows the user to select a specific category 
    and enter a search term. The results are then displayed in a clear and readable format. 
    This tool is particularly useful for network administrators and security analysts who need to quickly find rules that match a specific search term.
    """)

df['category'] = df['rule_text'].apply(lambda x: re.findall(r'msg:"(?:ET\s+)?([A-Z_\-]+)[^A-Z_\- ]*', x)[0] if re.findall(r'msg:"(?:ET\s+)?([A-Z_\-]+)[^A-Z_\- ]*', x) else None)

categories = df['category'].dropna().unique()
selected_category = st.selectbox('Select a category', options=categories)
st.write(df[df['category'] == selected_category])
search_term = st.text_input('Enter your search term here')
st.write(df[df['rule_text'].str.contains(search_term, case=False)])

# Uncomment to display a giant table.
#st.table(df)       