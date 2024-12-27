# METADATA [app.py] - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Description: This code script contains the implementation of a web application for Exploratory Data Analysis (EDA)
    # using Python's AutoViz.

    # Developed By: 
        # Name: Mohini T
        # Role: Intern, PreProd Corp
        # Code ownership rights: Mohini T, PreProd Corp
    
    # Version:
        # v1.0 Initial version. [Date: 27-12-2024]

# CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Dependencies:
        # Python 3.11.0
        # Libraries:
            # Streamlit 1.40.2
            # Pandas 2.2.3

# Importing the necessary libraries
import streamlit as st # For creating the web app
import pandas as pd # For data manipulation

# Importing the function to visualize the data
from eda import visualize_data

# Initialize session state for data if it doesn't exist
if 'data' not in st.session_state:
    st.session_state.data = None

# Setting the page configuration for the web app
st.set_page_config(page_title="AutoViz", page_icon=":bar_chart:", layout="centered")

# Adding a heading to the web app
st.markdown("<h1 style='text-align: center; color: white;'>Exploratory Data Analysis using Python's AutoViz 📊</h1>", unsafe_allow_html=True)
st.divider()

# Creating tabs for the web app
tab1, tab2 = st.tabs(["Data Ingestion 📂", "Exploratory Data Analysis 📋"])

# Data Ingestion tab
with tab1:
    st.subheader("Data Ingestion 📂")
    
    with st.container(border=True):
        # Radio button to choose between uploading a file or entering a file path
        dataset_choice = st.radio("Choose an option to upload the data", ["Upload the file", "Enter the path"], horizontal=True)
        dataset_bool = True if dataset_choice == "Upload the file" else False

        # File uploader for CSV files
        data_upload = st.file_uploader("Upload a CSV file",
                                    type="csv",
                                    help="Upload a CSV file to generate a report.",
                                    disabled=not dataset_bool)
        
        # Text input for entering the file path
        data_filepath = st.text_input("Enter the path to the CSV file",
                                help="Enter the complete path to the source data.",
                                disabled=dataset_bool)
        
        if st.button("Ingest", use_container_width=True):
            # Read the uploaded file or the file from the entered path
            if dataset_bool:
                st.session_state.data = pd.read_csv(data_upload)
            else:
                st.session_state.data = pd.read_csv(data_filepath)
            
            # Display success or error message based on data ingestion
            if st.session_state.data is not None:
                st.success("Data ingested successfully!", icon="✅")
            else:
                st.error("Error ingesting data!", icon="❌")

    # Form to display data configuration (number of rows, columns, and first 5 rows)
    with st.form(key="data_config"):
        st.subheader("Data Configuration")
        if st.form_submit_button("Run", use_container_width=True):
            if st.session_state.data is not None:
                st.write(f"Number of rows: {st.session_state.data.shape[0]}")
                st.write(f"Number of columns: {st.session_state.data.shape[1]}")
                st.write(st.session_state.data.head())
            else:
                st.error("No data available to display!", icon="❌")
    
    # Display the data types of the columns
    with st.form(key="data_types"):
        st.subheader("Data Types")
        if st.form_submit_button("Run", use_container_width=True):
            if st.session_state.data is not None:
                st.write(st.session_state.data.dtypes)
            else:
                st.error("No data available to display!", icon="❌")
    
    # Form to drop the uploaded file and clear the data from session state
    with st.form(key="drop_data"):
        st.subheader("Drop Uploaded File")
        if st.form_submit_button("Drop", use_container_width=True):
            if st.session_state.data is not None:
                st.session_state.data = None
                st.success("Data dropped successfully!", icon="✅")
            else:
                st.error("No file available to drop!", icon="❌")

# Exploratory Data Analysis tab
with tab2:
    st.subheader("Exploratory Data Analysis 📋")

