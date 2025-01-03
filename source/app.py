# METADATA [app.py] - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Description: This code script contains the implementation of a web application for Exploratory Data Analysis (EDA)
    # using Python's AutoViz.

    # Developed By: 
        # Name: Mohini T
        # Role: Intern, PreProd Corp
        # Code ownership rights: Mohini T, PreProd Corp
    
    # Version:
        # v1.0 Initial version. [Date: 27-12-2024]
        # v1.1 Added individual forms for all arguments and terminal output display during visualization generation. [Date: 03-01-2025]

# CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Dependencies:
        # Python 3.11.0
        # Libraries:
            # Streamlit 1.40.2
            # Pandas 2.2.3
            # io
            # sys

# Importing the necessary libraries
import streamlit as st # For creating the web app
import pandas as pd # For data manipulation
import io # For input/output operations
import sys # For capturing terminal output

# Importing the function to visualize the data
from eda import visualize_data

# Initializing the session state to store the data
if "data" not in st.session_state:
    st.session_state.data = None

# Setting the page configuration for the web app
st.set_page_config(page_title="AutoViz", page_icon=":bar_chart:", layout="centered")

# Adding a heading to the web app
st.markdown("<h1 style='text-align: center; color: white;'>Automatic Data Visualization and EDA using Python's AutoViz 📊</h1>", unsafe_allow_html=True)
st.divider()

# Creating tabs for the web app
tab1, tab2 = st.tabs(["Data Ingestion 📂", "AutoViz 📋"])

# Data Ingestion tab
with tab1:
    st.subheader("Data Ingestion 📂")

    # Form to upload the file path as text input
    with st.form(key="file_path"):
        st.subheader("Enter File Path")
        file_path = st.text_input("Enter the file path of the dataset",
                                help="Enter the complete file path of the dataset to be visualized.")
        
        if st.form_submit_button("Ingest", use_container_width=True):
            # Display success or error message based on validity of the file path.
            try:
                pd.read_csv(file_path) # If the file is found at the file path, only then the file path is considered valid.
                st.success("File path is valid!", icon="✅")
            except:
                st.error("Invalid file path!", icon="❌")
    
    # Form to display data configuration (number of rows, columns, and first 5 rows)
    with st.form(key="display_data"):
        st.subheader("Display Data Configuration")
        if st.form_submit_button("Display", use_container_width=True):
            try:
                data = pd.read_csv(file_path) # Reading the data from the file path
                st.session_state.data = data # Storing the data in session state for later use
                st.write(f"Number of rows: {data.shape[0]}") # Displaying the number of rows in the dataset
                st.write(f"Number of columns: {data.shape[1]}") # Displaying the number of columns in the dataset
                st.write(data.head()) # Displaying the first 5 rows of the dataset
            except:
                st.error("No data available to display!", icon="❌")


# AutoViz tab
with tab2:
    st.subheader("AutoViz 📋")

    # Individual forms for all the arguments of the visualize_data function

    # Separator (Delimiter)
    with st.form(key="separator"):
        st.subheader("Separator")
        sep = st.text_input("Enter the separator used in the dataset",
                                placeholder=",",
                                help="Enter the delimiter used in the dataset (default is ',').")
        
        if st.form_submit_button("Set", use_container_width=True):
            # Display success or error message based on the separator being set.
            if sep is not None:
                st.success("Separator set successfully!", icon="✅")
            else:
                st.error("Error setting separator!", icon="❌")
    
    # Dependent Variable (Target)
    with st.form(key="dependent_variable"):
        st.subheader("Dependent Variable")
        # Choosing the dependent variable is a drop down menu with the column names of the dataset.
        # This argument is optional, so the user can choose to not set it.
        dep_var = st.selectbox("Select the dependent variable",
                                options=[""] + (list(st.session_state.data.columns) if st.session_state.data is not None else []),
                                help="Select the dependent variable from the dataset.")
                                
        if st.form_submit_button("Set", use_container_width=True):
            # Display success message for setting the dependent variable only if it is valid.
            if dep_var != "":
                st.success("Dependent variable set successfully!", icon="✅")
            else:
                st.error("Error setting dependent variable!", icon="❌")
    
    # Header (Column Names)
    with st.form(key="header"):
        st.subheader("Header")
        header = st.number_input("Enter the row number to use as the column names",
                                value=0,
                                help="Enter the row number to use as the column names (default is 0).")
        
        if st.form_submit_button("Set", use_container_width=True):
            # Display success message for setting the header only if it is valid.
            if header is not None:
                st.success("Header set successfully!", icon="✅")
            else:
                st.error("Error setting header!", icon="❌")

    # Verbose Level (Verbosity: Quality of being wordy and using more words than needed)
    with st.form(key="verbose"):
        st.subheader("Verbose")
        verbose = st.selectbox("Select the verbosity level",
                                options=[0, 1, 2],
                                index=0,
                                help="Select the verbosity level (0: no messages, 1: messages, 2: detailed messages).")
        
        if st.form_submit_button("Set", use_container_width=True):
            # Display success message for setting the verbose level only if it is valid.
            if verbose is not None:
                st.success("Verbose level set successfully!", icon="✅")
            else:
                st.error("Error setting verbose level!", icon="❌")
    
    # Lowess Flag (Lowess Smoothing: Locally Weighted Scatterplot Smoothing)
    with st.form(key="lowess"):
        st.subheader("Lowess")
        lowess = st.checkbox("Use Lowess",
                            help="Flag to indicate whether to use lowess or not (default is False).")
        
        if st.form_submit_button("Set", use_container_width=True):
            # Display success message for setting the lowess flag only if it is valid.
            if lowess is not None:
                st.success("Lowess flag set successfully!", icon="✅")
            else:
                st.error("Error setting lowess flag!", icon="❌")
    
    # Chart Format (Format of the Charts: SVG, PNG, JPG, Bokeh, Server, HTML)
    with st.form(key="chart_format"):
        st.subheader("Chart Format")
        # Chart format should be a drop down with default value of 'svg'.
        chart_format = st.selectbox("Select the format of the charts",
                                    options=['svg', 'png', 'jpg', 'bokeh', 'server', 'html'],
                                    index=3,
                                    help="Select the format of the charts ('svg', 'png', 'jpg', 'bokeh', 'server', or 'html').")
        
        if st.form_submit_button("Set", use_container_width=True):
            # Display success message for setting the chart format only if it is valid.
            if chart_format is not None:
                st.success("Chart format set successfully!", icon="✅")
            else:
                st.error("Error setting chart format!", icon="❌")
    
    # Max Rows Analyzed (For Performance Optimization and Speed Improvement for Large Datasets)
    with st.form(key="max_rows_analyzed"):
        st.subheader("Max Rows Analyzed")
        max_rows_analyzed = st.number_input("Enter the maximum number of rows to be analyzed",
                                            value=150000,
                                            help="Enter the maximum number of rows to be analyzed (default is 150000).")
        
        if st.form_submit_button("Set", use_container_width=True):
            # Display success message for setting the maximum rows only if it is valid.
            if max_rows_analyzed is not None:
                st.success("Maximum rows set successfully!", icon="✅")
            else:
                st.error("Error setting maximum rows!", icon="❌")
    
    # Max Columns Analyzed (For Performance Optimization and Speed Improvement for Large Datasets)
    with st.form(key="max_cols_analyzed"):
        st.subheader("Max Columns Analyzed")
        max_cols_analyzed = st.number_input("Enter the maximum number of columns to be analyzed",
                                            value=30,
                                            help="Enter the maximum number of columns to be analyzed (default is 30).")
        
        if st.form_submit_button("Set", use_container_width=True):
            # Display success message for setting the maximum columns only if it is valid.
            if max_cols_analyzed is not None:
                st.success("Maximum columns set successfully!", icon="✅")
            else:
                st.error("Error setting maximum columns!", icon="❌")
    
    # Save Directory (Directory to Save the Plots)
    with st.form(key="save_directory"):
        st.subheader("Save Directory")
        save_dir = st.text_input("Enter the directory to save the plots",
                                value="plots",
                                help="Enter the directory to save the plots (default is 'plots').")
        
        if st.form_submit_button("Set", use_container_width=True):
            # Display success message for setting the save directory only if it is valid.
            if save_dir is not None:
                st.success("Save directory set successfully!", icon="✅")
            else:
                st.error("Error setting save directory!", icon="❌")
    
    # Form with button to visualize the data, and show the plots
    with st.form(key="visualize_data"):
        st.subheader("Visualize Data")

        # Button to generate and display visualizations
        if st.form_submit_button("Generate Visualizations", use_container_width=True):
            try:
                # Retrieve all user inputs
                data = st.session_state.data
                arguments = {
                    "file_path": file_path,  # File path of the dataset
                    "sep": sep,  # Separator used in the dataset
                    "dep_var": dep_var,  # Dependent variable (target column)
                    "header": header,  # Row number to use as column names
                    "verbose": verbose,  # Verbosity level
                    "lowess": lowess,  # Flag to use Lowess smoothing
                    "chart_format": chart_format,  # Format of the charts
                    "max_rows_analyzed": max_rows_analyzed,  # Maximum number of rows to analyze
                    "max_cols_analyzed": max_cols_analyzed,  # Maximum number of columns to analyze
                    "save_dir": save_dir,  # Directory to save the plots
                }

                # Redirect stdout to capture terminal output
                output_buffer = io.StringIO()
                sys.stdout = output_buffer

                # Call the visualize_data function to generate visualizations
                st.info("Generating visualizations... This may take a moment.", icon="⏳")
                visualize_data(**arguments)
                st.success("Visualizations generated successfully!", icon="✅")

                # Restore stdout to its original state
                sys.stdout = sys.__stdout__

                # Get and display captured output from the terminal
                terminal_output = output_buffer.getvalue()
                output_buffer.close()
                st.subheader("Output Code")
                st.code(terminal_output, language="plaintext")

                # Display information about where the visualizations are saved
                st.subheader("Generated Visualizations")
                st.markdown(
                    f"Visualizations saved to directory: `{save_dir}`. Please check the plots there or specify another directory to save them.",
                    unsafe_allow_html=True,
                )
            except Exception as e:
                # Restore stdout in case of an error
                sys.stdout = sys.__stdout__
                st.error(f"An error occurred: {e}", icon="❌")