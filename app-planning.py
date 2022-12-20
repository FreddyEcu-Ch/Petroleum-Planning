# import Python Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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