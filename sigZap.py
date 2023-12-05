import streamlit as st
import sqlite3
import pandas as pd
import re

st.set_page_config(page_title="sigZap", layout="wide")

# Connect to SQLite database and fetch data
conn = sqlite3.connect('rules.db')
query = "SELECT * FROM rule_sets"
df = pd.read_sql_query(query, conn)
conn.close()

# Extract categories from rule texts
df['category'] = df['rule_text'].apply(lambda x: re.findall(r'msg:"(?:ET\s+)?([A-Z_\-]+)[^A-Z_\- ]*', x)[0] if re.findall(r'msg:"(?:ET\s+)?([A-Z_\-]+)[^A-Z_\- ]*', x) else None)

# Streamlit application starts here
st.title('sigZap')
st.markdown("""
    This Streamlit application facilitates searches across multiple network signature sets. 
    Users can search by category or use a custom search term to query the database. 
    The results are displayed in a clear and readable format, making it a valuable tool for network administrators and security analysts.
""")

# Tab setup
tab1, tab2 = st.tabs(["Category Search", "Search Ruleset"])

with tab1:
    st.subheader("Category Search")
    categories = df['category'].dropna().unique()
    selected_category = st.selectbox('Select a category:', options=categories)
    filtered_df = df[df['category'] == selected_category]
    st.write(filtered_df)

with tab2:
    st.subheader("Search Ruleset")
    search_term = st.text_input('Enter your search term:')
    if search_term:
        search_results = df[df['rule_text'].str.contains(search_term, case=False)]
        st.write(search_results)

st.sidebar.image("assets/images/logo.png", width=300)

# Uncomment to display the entire dataset
# st.table(df)
