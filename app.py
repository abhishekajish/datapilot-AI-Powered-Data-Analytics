import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import streamlit as st
import pandas as pd

from backend.profiling.profiler import generate_profile
from backend.services.cleaner import clean_data


st.set_page_config(
    page_title="AI Data Scientist Copilot",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Data Scientist Copilot")

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    # Save uploaded file
    os.makedirs("data/raw", exist_ok=True)

    file_path = f"data/raw/{uploaded_file.name}"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Read dataset
    df = pd.read_csv(uploaded_file)

    # Generate profile
    profile = generate_profile(df)

    # Clean dataset
    cleaned_df, duplicates_removed = clean_data(df)

    st.success("File uploaded successfully!")

    st.header("Dataset Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", profile["rows"])

    with col2:
        st.metric("Columns", profile["columns"])

    with col3:
        st.metric("Duplicate Rows", profile["duplicates"])

    st.header("Missing Values")

    missing_values = profile["missing_values"]
    missing_values = missing_values[missing_values > 0]

    if len(missing_values) == 0:
        st.success("No missing values found!")
    else:
        st.write(missing_values)

    st.header("Data Types")

    st.write(profile["data_types"])

    st.header("Column Names")

    for col in df.columns:
        st.write(f"• {col}")

    st.header("Cleaning Results")

    st.metric(
        "Duplicates Removed",
        duplicates_removed
    )

    st.header("Original Dataset")

    st.dataframe(df.head())

    st.header("Cleaned Dataset")

    st.dataframe(cleaned_df.head())