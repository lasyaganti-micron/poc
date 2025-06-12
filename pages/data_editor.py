import streamlit as st
import pandas as pd
import os
from data_loader import get_excel_files, load_data, save_data

st.title("Data Editor")

files = get_excel_files()
selected_file = st.selectbox("Choose an Excel file", files)

if selected_file:
    df = load_data(selected_file)
    edited_df = st.data_editor(df, num_rows="dynamic", key=selected_file)

    if st.button("Save Changes"):
        save_data(selected_file, edited_df)
        st.success("Data saved successfully!")
