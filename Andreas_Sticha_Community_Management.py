import streamlit as st
import datetime as dt
from helpers import *


st.set_page_config(layout="wide")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.markdown(
    "<h1 style='text-align: center; color: green;'>Andreas Sticha: Community Management Dashboard</h1>",
    unsafe_allow_html=True,
)

filter_day, filter_Interactions, filter_date = display_filters()
dataframe_path = "https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/eb1L1WPcmTfYrbC51oB9rg/andreas_sticha_keyword_search.csv"

selection_keywords = keywords


try:
    df_main = load_dataframe(dataframe_path)

    filtered_posts = filter_and_sort_posts(
        df_main, filter_day, filter_Interactions, filter_date
    )

    choice = st.sidebar.selectbox("Select your keyword:", selection_keywords)

    choosen_df = choice_selector(filtered_posts, choice=choice)

    if filtered_posts is not None:
        num_posts = choosen_df.shape[0]
        st.write(f"Total number of posts found: {num_posts}")

        display_post_chunks(choosen_df)

    else:
        st.write("An error occurred!")

except Exception as e:
    st.write(f"Error encountered!!!, {e}")
