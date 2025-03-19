import streamlit as st


principal = st.title("Lista de tarea")


# row, row2 = st.columns(2)
# row3, row4 = st.columns(2)

if "anadir_tarea" not in st.session_state:
    st.session_state.anadir_tarea = []

if "tarea" not in st.session_state:
    st.session_state.tarea = ""

with st.form("formulario_agregar_texto"):
    st.session_state.tarea = st.text_input("")
    boton1 = st.form_submit_button("➕")


if boton1:
    if st.session_state.tarea:
        st.session_state.anadir_tarea.append(st.session_state.tarea)
        st.session_state.tarea = ""
    else:
        st.error("Debes introducir una tarea.")


for i, tarea in enumerate(st.session_state.anadir_tarea):

    col1, col2, col3 = st.columns([6, 6, 2])

    with col1:
        edictar = st.text_input(f"tarea {i+1}", value=tarea, key=f"edictar_{i}")
    with col2:
        if st.button("Guardar", key=f"guardar_{i}"):
            st.session_state.anadir_tarea[i] = edictar
    with col3:
        if st.button("Borrar", key=f"Borrar_{i}"):
            del st.session_state.anadir_tarea[i]
            st.rerun()
