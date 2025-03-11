from explore_page import show_explore
import streamlit as st


page= st.selectbox("Explore or Predict", ("Predict", "Explore" ))


if page == "Predict":
    show_explore