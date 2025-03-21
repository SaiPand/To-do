import streamlit as st
import time


def page2():
    st.title("_Lista de tarea_")


pg = st.navigation(
    [
        st.Page(page2, title="To-Do", icon=":material/favorite:"),
    ]
)
pg.run()


if "anadir_tarea" not in st.session_state:
    st.session_state.anadir_tarea = []


if "tarea" not in st.session_state:
    st.session_state.tarea = ""

with st.form("formulario_agregar_texto"):
    st.session_state.tarea = st.text_input("", placeholder="Escribe tu siguiente tarea")
    boton1 = st.form_submit_button("_Agregar_", type="secondary")


if boton1:
    if st.session_state.tarea:
        st.session_state.anadir_tarea.append(st.session_state.tarea)
        st.session_state.tarea = ""
    else:
        # st.error("Debes introducir una tarea")
        st.toast("Debes introducir una tarea", icon="🚨")
        time.sleep(0.5)


for i, tarea in enumerate(st.session_state.anadir_tarea):

    col1, col2, col3, col4 = st.columns([2, 2, 3, 3])

    with col2:
        check = st.checkbox(tarea, key=f"check_{i}_{tarea}")
    with col3:

        # if st.button("Edictar", key=f"edictar_{i}"):
        with st.popover("✍️ Edictar Tarea"):
            nuevo_texto = st.text_input(
                f"tarea {i+1}", value=tarea, key=f"edictar_expanded_{i}"
            )
            if st.button("💾 Guardar Cambio", key=f"guardar_{i}"):
                st.session_state.anadir_tarea[i] = nuevo_texto
                st.toast("Tarea actualizada", icon="✅")
                time.sleep(0)

    with col4:
        if st.button("🗑️ Borrar", key=f"Borrar_{i}"):

            del st.session_state.anadir_tarea[i]
            st.rerun()

bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://as1.ftcdn.net/jpg/02/74/70/20/1000_F_274702029_dC9sFwkI5xpuHuHvGFcma0zmYTSrE16i.webp");
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
