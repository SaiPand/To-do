import streamlit as st


principal = st.title("Lista de tarea")


if "anadir_tarea" not in st.session_state:
    st.session_state.anadir_tarea = []


if "tarea" not in st.session_state:
    st.session_state.tarea = ""

with st.form("formulario_agregar_texto"):
    st.session_state.tarea = st.text_input("", placeholder="Escribe tu siguiente tarea")
    boton1 = st.form_submit_button("Agregar", type="secondary")


if boton1:
    if st.session_state.tarea:
        st.session_state.anadir_tarea.append(st.session_state.tarea)
        st.session_state.tarea = ""
    else:
        st.error("Debes introducir una tarea.")


for i, tarea in enumerate(st.session_state.anadir_tarea):

    col1, col2, col3, col4 = st.columns([1, 3, 2, 2])

    with col1:
        check = st.checkbox("", key=f"check_{i}_{tarea}")
    with col2:
        edictar = st.text_input(
            f"tarea {i+1}", value=tarea, key=f"edictar_{i}", disabled=False
        )
        if check:
            st.session_state.anadir_tarea[i] = st.session_state.anadir_tarea[i]

    with col3:
        if st.button("💾 Guardar", key=f"guardar_{i}"):
            st.session_state.anadir_tarea[i] = edictar
            st.success("Texto actualizado")

    with col4:
        if st.button("🗑️ Borrar", key=f"Borrar_{i}"):
            del st.session_state.anadir_tarea[i]
            st.rerun()

bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://e1.pxfuel.com/desktop-wallpaper/521/789/desktop-wallpaper-monte-tepuy-roraima-paisajes-de-venezuela-mt-roraima.jpg");
background-size: cover;
}
[data-testid="stHeader"]{
  background-color: rgba(0,0,0,0);
}
.caption-style{
  color: black;
  text-align: justify;
  font-size: 20px;
}
.prediction-style{
  color: black;
  text-align: justify;
  font-size: 20px;
}

.description-style{
  color: black;
  text-align: justify;
  font-size: 20px;
}

.block-container {
    background-color: #FAFAFA;
    margin: 25px;
    border: 2px solid grey;
    border-radius: 25px;
    padding-top: 25px;
}


</style>
"""
st.markdown(bg_img, unsafe_allow_html=True)
