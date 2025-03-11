import streamlit as st
import io
import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    dataset= pd.read_csv (r"healthcare-dataset-stroke-data.csv")
    dataset.head()

    return dataset
    