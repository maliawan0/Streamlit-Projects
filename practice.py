import pandas as pd
import streamlit as st

df = pd.DataFrame({"col1": [1, 2, 3]})
df  # 👈 Draw the dataframe

x = 10
"x", x  # 👈 Draw the string 'x' and then the value of x


y = 10

"y"

import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Draw a Matplotlib chart


st.latex(r"""
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    """)

st.write("Hey start doing hard work")

st.slider("this is a very simple slider ", 0, 100, (23, 77))

st.divider()
st.write("Hey start doing hard work after a slider ")


st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")


df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
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
import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 4), columns=["col1", "col2", "col3", "col4"]
)

st.scatter_chart(
    chart_data,
    x="col1",
    y=["col2", "col3"],
    size="col4",
    color=["#FF0000", "#0000FF"],  # Optional
)
