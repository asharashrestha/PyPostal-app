import streamlit as st
from postal.expand import expand_address
from postal.parser import parse_address

st.set_page_config(layout="wide")
# model =st.sidebar.selectbox("Select library: ",["PyPostal","Address-Net"])
file_path = "/Users/ashara/Documents/AtosSyntel/AdressParsr/result_txt.csv"
# if model == "PyPostal":
addr = st.sidebar.text_area("Enter Address")
parse_addr = parse_address(addr)
for elem in parse_addr:
    st.write(str(elem[1]) + ": " + str(elem[0]))
st.write("\n")