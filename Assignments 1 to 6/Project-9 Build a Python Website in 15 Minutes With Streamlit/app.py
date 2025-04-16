# Import necessary libraries
import streamlit as st  # For building the web app
import pandas as pd     # For reading and working with CSV data
import matplotlib.pyplot as plt  # Optional: used for plotting (not used here)

# Set the title of the web app
st.title("Simple Data Dashboard")

# File uploader to let the user upload a CSV file
upload_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Check if the file is uploaded
if upload_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(upload_file)

    # Show first 5 rows of the data
    st.subheader("📊 Data Preview:")
    st.write(df.head())

    # Show basic statistical details (mean, max, min, etc.)
    st.subheader("📈 Data Summary")
    st.write(df.describe())

    # Add filter section
    st.subheader("🔍 Filter Data")

    # Get list of column names
    columns = df.columns.tolist()

    # Let user select a column to filter
    selected_column = st.selectbox("Select a column to filter", columns)

    # Get unique values from selected column
    unique_values = df[selected_column].unique()

    # Let user select a value to filter on
    selected_value = st.selectbox("Select a value to filter", unique_values)

    # Filter the data based on the selected value
    filtered_data = df[df[selected_column] == selected_value]

    # Display the filtered data
    st.write(filtered_data)

    # Add plotting section
    st.subheader("📉 Plot Data")

    # Let user choose x and y columns for the chart
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    # If user clicks the button, generate the line chart
    if st.button("Generate Plot"):
        # Set x_column as index and plot y_column as line chart
        st.line_chart(filtered_data.set_index(x_column)[y_column])

# If no file is uploaded, show a waiting message
else:
    st.write("Waiting on file to be uploaded...")
