# import Python Libraries
import numpy as np
import pandas as pd
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
upload_file = st.sidebar.file_uploader("Upload your file")

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
    fig = px.histogram(
        df, x=df.iloc[:, -1], labels={"x": "Gender"}, color=df.iloc[:, -1]
    )
    st.plotly_chart(fig)
    st.subheader("**Summary**")
    g = [n for n in df.iloc[:, -1].value_counts()]
    g.reverse()
    st.write(
        f"Currently, there are **{g[1]} male and {g[0]} female students** enrolled in petroleum engineering."
    )
    st.subheader("**Statistical Summary**")
    fig_2 = px.pie(df, values=g, names=df.iloc[:, -1].unique())
    st.plotly_chart(fig_2)
    col1, col2 = st.columns(2)
    col1.metric("Male", g[1])
    col2.metric("Female", g[0])


def average(df):
    df_c = df.loc[df.iloc[:, 3] != 0]
    fig = px.bar(
        df_c,
        x=df_c.iloc[:, 3],
        y=df_c.iloc[:, 2],
        labels={"x": "Academic Performance", "y": "student"},
    )
    st.plotly_chart(fig)
    st.subheader("**Summary**")
    col1, col2, col3 = st.columns(3)
    max_g = df_c.loc[df_c.iloc[:, 3] == df_c.iloc[:, 3].max()].iloc[:, 2].values[0]
    min_g = df_c.loc[df_c.iloc[:, 3] == df_c.iloc[:, 3].min()].iloc[:, 2].values[0]
    col1.metric(f"Max Grade", df_c.iloc[:, 3].max())
    col2.metric("Average", round(df_c.iloc[:, 3].mean(), 2))
    col3.metric(f"Min Grade", df_c.iloc[:, 3].min())
    st.success(f" **Max grade**: {max_g}")
    st.success(f" **Min grade**: {min_g}")


def students(df):
    st.subheader("**Students Information**")
    est = st.selectbox("Select a student", options=df.iloc[:, 2])
    st.subheader("**Show Information**")
    df_est = df.loc[df.iloc[:, 2] == est]
    features = np.array(
        ["ID", "Name", "Grade", "% Career Advancement", "Credits to take", "Gender"]
    )
    ind = np.array([1, 2, 3, 4, 5, 7])
    infor = [
        st.write(f"{col}: {df_est.iloc[:, index].values[0]}")
        for index, col in zip(ind, features)
    ]


# Call dataframe
if upload_file:
    df = pd.read_csv(upload_file, encoding="latin-1")

# Call options of web app
if options == "Data":
    data(df)

elif options == "Plots":
    if st.checkbox("Gender"):
        st.subheader("**Students per Gender**")
        gender(df)

    elif st.checkbox("Academic Performance"):
        average(df)

    elif st.checkbox("Students Information"):
        students(df)
