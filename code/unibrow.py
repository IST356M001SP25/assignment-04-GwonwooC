'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

file = st.file_uploader("Upload a file:", type=["csv", "xlsx", "json"])
if file:
    file_type = pl.get_file_extension(file.name)
    df = pl.load_file(file, file_type)
    columns = pl.get_column_names(df)
    selected_columns = st.multiselect("Select columns to display", columns, default=columns)
    
    if st.toggle("Enable Data Filtering"):
        filter_options = st.columns(3)
        text_columns = pl.get_columns_of_type(df, 'object')
        chosen_column = filter_options[0].selectbox("Select column to filter", text_columns)
        if chosen_column:
            unique_values = pl.get_unique_values(df, chosen_column)
            chosen_value = filter_options[1].selectbox("Select value to filter On", unique_values)
            filtered_df = df[df[chosen_column] == chosen_value][selected_columns]
    else:
        filtered_df = df[selected_columns]
    
    st.dataframe(filtered_df)
    st.dataframe(filtered_df.describe())

