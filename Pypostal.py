import streamlit as st
from postal.expand import expand_address
from postal.parser import parse_address
import csv

st.set_page_config(layout="wide")
model =st.sidebar.selectbox("Select library: ",["PyPostal","Address-Net"])
file_path = "/Users/ashara/Documents/AtosSyntel/AdressParsr/result_txt.csv"
if model == "PyPostal":
    addr = st.sidebar.text_area("Enter Address")