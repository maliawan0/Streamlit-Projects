import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("My First Dashboard")

upload_file = st.file_uploader("Choose a file to upload", type="csv")

if upload_file is not None:
    df = pd.read_csv(upload_file)

    st.subheader("Data Preview")

    st.write(df.head())

    st.subheader("Data Description")

    st.write(df.describe())

    st.subheader("Filtered Data")
    columns = df.columns.tolist()
    selected_columns = st.selectbox("Select a Column you want to filter ", columns)
    unique_val = df[selected_columns].unique()

    selected_values = st.selectbox("Select a value you want to ", unique_val)

    filtered_df = df[df[selected_columns] == selected_values]
    st.write(filtered_df)

    st.subheader("Plot Data")

    x_column = st.selectbox("Select X-axis column", columns)
    y_column = st.selectbox("Select Y-axis column", columns)

    if st.button("Generate a Line chart "):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

else:
    st.write("Waiting for Upload")
