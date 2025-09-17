import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("CARS.csv")

# Page title
st.title("Car Brand Horsepower Explorer")

# Show a preview of the data
st.subheader("Dataset Preview")
st.write(df.head(2))

# Dropdown for selecting car brand
brands = df['Make'].unique()
selected_brand = st.selectbox("Select a Car Brand", brands)

# Filter data for selected brand
filtered_df = df[df['Make'] == selected_brand]

# Check if filtered data is available
if not filtered_df.empty:
    st.subheader(f"Horsepower by Model for {selected_brand}")

    # Create barplot
    fig, ax = plt.subplots(figsize=(10, 5))
    sb.barplot(x=filtered_df['Model'], y=filtered_df['Horsepower'], ax=ax)
    plt.xticks(rotation=90)
    st.pyplot(fig)
else:
    st.warning("No data available for the selected brand.")
