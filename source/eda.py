# METADATA [eda.py] - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Description: This code script

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
            # AutoViz 0.1.905

# Importing the necessary libraries
from autoviz.AutoViz_Class import AutoViz_Class

# Function to visualize the data
def visualize_data(file_path, sep=',', dep_var='', df=None, header=0, verbose=0, lowess=False, chart_format='svg', max_rows_analyzed=150000, max_cols_analyzed=30):
    AV = AutoViz_Class() # Creating an instance of the AutoViz class
    df = AV.AutoViz(
        filename=file_path,                  # File path of the dataset to be visualized (if not provided, the 'df' parameter is used)
        sep=sep,                             # Delimiter used in the dataset (default is ',')
        depVar=dep_var,                      # Dependent variable in the dataset (if not provided, the 'df' parameter is used)
        dfte=df,                             # DataFrame to be visualized (if not provided, the 'file_path' parameter is used)
        header=header,                       # Row number to use as the column names (default is 0)
        verbose=verbose,                     # Verbosity level (0: no messages, 1: messages, 2: detailed messages)
        lowess=lowess,                       # Flag to indicate whether to use lowess or not (default is False)
        chart_format=chart_format,           # Format of the charts (default is 'svg') - 'svg', 'png', 'jpeg', 'pdf' or 'webp'
        max_rows_analyzed=max_rows_analyzed, # Maximum number of rows to be analyzed (default is 150000)
        max_cols_analyzed=max_cols_analyzed  # Maximum number of columns to be analyzed (default is 30)
    )
    return df