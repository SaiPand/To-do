import streamlit as st


principal = st.title("Lista de tarea")

anadir_tarea = []
row, row2 = st.columns(2)
row3, row4 = st.columns(2)

with st.form("añadir_tarea"):
    tarea = row.text_input("")
    boton1 = st.form_submit_button
    boton2 = row2.button("➕ ", type="tertiary")


if boton1:
    if tarea:
        anadir_tarea.append(tarea)
    elif boton2:
        st.error("Debes introducir una tarea.")


for i, tarea in enumerate(anadir_tarea):
    st.write(f"{i+1}:{tarea}")

    # agree = st.checkbox(f"{i+1}:{tarea}")
