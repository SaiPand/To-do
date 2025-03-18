import streamlit as st


principal = st.title("Lista de tarea")


row, row2 = st.columns(2)
row3, row4 = st.columns(2)


lst = row.text_input("", placeholder="Lista de tarea")

if row2.button("➕", type="tertiary"):
    agree = st.checkbox(lst)
