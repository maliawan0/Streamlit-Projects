import streamlit as st
import pandas as pd
import numpy as np

# Generating random points around Lahore
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [31.5497, 74.3436],  # Coordinates for Lahore
    columns=["lat", "lon"],
)

# Displaying the map
st.map(df)
