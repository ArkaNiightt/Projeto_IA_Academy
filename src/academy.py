import streamlit as st
from streamlit_player import st_player
# import uuid


def carregar_modulos(df):
    """
    Carrega e exibe módulos de curso organizados por categoria em uma interface Streamlit.
    Esta função cria uma interface interativa que permite:
    - Selecionar categorias via dropdown
    - Visualizar módulos expandíveis por categoria
    - Acessar aulas individuais com:
        - Player de vídeo
        - Resumo do conteúdo
        - Notas de aula em formato código
    Args:
        df (pandas.DataFrame): DataFrame contendo as informações dos cursos com as colunas:
            - categoria: Categoria do curso
            - aula_modulo: Identificador do módulo
            - aula_index: Número/índice da aula
            - nome_curso: Nome da aula/curso
            - url_video: URL do vídeo da aula
            - resumo: Texto com resumo da aula
            - notas: Notas/código da aula em formato HTML
    Returns:
        None: A função modifica diretamente a interface Streamlit
    Example:
        >>> df = pd.DataFrame({...})  # DataFrame com dados do curso
        >>> carregar_modulos(df)
    """
    categorias = df["categoria"].unique()
    categoria_selecionada = st.selectbox("Selecione a categoria:", categorias)

    st.title(f"{str(categoria_selecionada).capitalize()}")
    try:
        for modulo in df[df["categoria"] == categoria_selecionada]["aula_modulo"].unique():
            aulas = df[df["aula_modulo"] == modulo]
            with st.expander(f"Modulo: {modulo}", icon="📚"):
                for _, aula in aulas.iterrows():
                    st.write(
                            f":blue[Aula #{aula['aula_index']}] {str(aula['nome_curso']).capitalize()}"
                        )
                    tab_aula, tab_resumo, tab_notas = st.tabs(["Aula", "Resumo", "Notas"])
                    with tab_aula:
                        st_player(aula["url_video"])
                        st.markdown("---")
                    with tab_resumo:
                        # st.text_area(label="Resumo da aula", value=aula["resumo"], height=600, key=str(uuid.uuid4()))
                        st.markdown(aula["resumo"], help="Resumo da aula")
                        st.markdown("---")
                    with tab_notas:
                        st.code(aula["notas"], language="html")
                        st.write("---")
    except: 
        st.error("Erro ao carregar módulos do curso", icon="❌")
