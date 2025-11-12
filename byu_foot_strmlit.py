import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load data (make sure the CSV is in the repo)
df = pd.read_csv("byu_football_stats_2025.csv")

def main():
    st.title("BYU Football Stats 2025")
    st.write("Explore summary statistics and basic EDA for the 2025 BYU football season.")

    # Show the data
    st.subheader("Full Dataset")
    st.dataframe(df)

    # Summary stats
    st.subheader("Summary Statistics")
    st.write(df.describe())

    # Quick visualization example
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if numeric_cols:
        st.subheader("Histogram of a Numeric Column")
        column = st.selectbox("Choose a column", numeric_cols)
        fig, ax = plt.subplots()
        ax.hist(df[column].dropna(), bins=20)
        ax.set_title(f"Distribution of {column}")
        st.pyplot(fig)

if __name__ == "__main__":
    main()
