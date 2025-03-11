import streamlit as st


principal = st.title("Lista de tarea")


row, row2 = st.columns(2)
row3, row4 = st.columns(2)

with row:
    lst = st.text_input("", placeholder="Lista de tarea")


# with row2:
#     if st.button("➕", type="tertiary"):
#         lst


with row3:
    agree = st.checkbox(lst)
