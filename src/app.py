import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import streamlit as st
from academy import carregar_modulos, page_cadastrar
from database.connection import get_all_data

st.set_page_config(
    page_title="IA - Academy",
    page_icon="👾",
    layout="centered",
    initial_sidebar_state="expanded",
)

with open("./config/config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)


def auth():
    authenticator = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
        auto_hash=True,
    )
    return authenticator


authenticator = auth()


def reset_password():
    if st.button("Reset Password", type="primary", use_container_width=True):
        if st.session_state["authentication_status"]:
            try:
                if authenticator.reset_password(st.session_state["username"]):
                    st.success("Senha alterada com sucesso", icon="✅")
            except Exception as e:
                st.error(e, icon="❌")


def check_user(df):
    if st.session_state["authentication_status"]:
        with st.spinner("Carregando..."):
            st.success("Usuário autenticado", icon="✅")
            with st.sidebar:
                authenticator.logout(location="sidebar")
                reset_password()
            if st.session_state["name"] == "Victor Bruno":
                st.header(
                    f' Bem-vindo **{st.session_state["name"]}** 🦍', divider=True)
            elif st.session_state["name"] == None:
                pass
            elif st.session_state["name"] == "Joao Augusto":
                st.header(
                    f' Bem-vindo **{st.session_state["name"]}** 👑', divider=True)
            else:
                st.header(
                    f' Bem-vindo **{st.session_state["name"]}** 👋', divider=True)

            carregar_modulos(df)
    elif st.session_state["authentication_status"] is False:
        st.error("Usuário/senha está incorreto", icon="❌")
    elif st.session_state["authentication_status"] is None:
        st.warning("Por favor insira seu username e senha", icon="⚠️")


def render():
    try:
        authenticator.login(captcha=True)
        df = get_all_data()
        check_user(df)
    except Exception as e:
        st.error(e)


if __name__ == "__main__":
    render()
