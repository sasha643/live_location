import streamlit as st

import streamlit.components.v1 as components

st.title('Location on Map')

HtmlFile = open('geo.html', 'r', encoding='utf-8')

source_code = HtmlFile.read()

components.html(source_code,height=500)