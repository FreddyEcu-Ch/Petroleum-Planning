# import Python Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly_express as px
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# Insert an icon
icon = Image.open("Resources/oil icon.png")

# State the design of the app
st.set_page_config(page_title="PE App", page_icon=icon)

# Insert css codes to improve the design of the app
st.markdown(
    """
<style>
h1 {text-align: center;
}
body {background-color: #DCE3D5;
      width: 1400px;
      margin: 15px auto;
}
</style>""",
    unsafe_allow_html=True,
)

# Title of the app
st.title("**Petroleum Engineering Planning**")

st.write("---")

# Add information of the app
st.markdown(
    """ This app is used to plan all the activities related to the petroleum engineering program at ESPOL.

**Python Libraries:** streamlit, pandas, matplotlib
"""
)

# Add additional information
expander = st.expander("About")
expander.write("This app is useful for planning")

# Insert image
image = Image.open("Resources/platform.jpg")
st.image(image, width=100, use_column_width=True)

# Sidebar
Logo = Image.open("Resources/ESPOL.png")
st.sidebar.image(Logo)

# Add title to the sidebar section
st.sidebar.title(":arrow_down: **Navigation**")

# Upload files
upload_file = st.sidebar.file_uploader("Upload your file" )

# Pages
with st.sidebar:
    options = option_menu(
        menu_title="Menu",
        options=["Home", "Data", "Plots"],
        icons=["house", "tv-fill", "box"],
    )


# Useful functions
def data(df):
    st.dataframe(df)
    st.subheader("**Data Summary**")
    st.write(df.describe())


def gender(df):
    fig = px.histogram(df, x=df.iloc[:, -1], labels={"x": "Gender"}, color=df.iloc[:, -1])
    st.plotly_chart(fig)
    st.subheader("**Summary**")
    g = [n for n in df.iloc[:, -1].value_counts()]
    st.write(f"Currently, there are **{g[0]} male and {g[1]} female students** enrolled in petroleum engineering.")


# Call dataframe
if upload_file:
    df = pd.read_csv(upload_file, encoding='latin-1')

# Call options of web app
if options == "Data":
    data(df)

elif options == "Plots":
    if st.checkbox("Gender"):
        st.subheader("**Students per Gender**")
        gender(df)
