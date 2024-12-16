import streamlit as st
from streamlit_player import st_player
from database.connection import insert_data

# import uuid


def page_cadastrar():

    # "nome_curso": nome_curso,
    # "categoria": categoria,
    # "aula_index": aula_index,
    # "aula_modulo": aula_modulo,
    # "url_video": url_video,
    # "resumo": resumo,
    # "notas": notas,

    st.title("Cadastrar Curso")
    st.write("Preencha os campos abaixo para cadastrar um novo curso. Se você não tem as informações necessárias, pode deixar os campos em branco. Não preecha as informações sem consultar o autor do projeto.")
    nome_curso = st.text_input(
        label="Nome da Aula",
        placeholder="Digite o nome da aula",
        key="nome_curso",
        help="Digite o nome da aula"
    )
    categoria = st.text_input(
        label="Curso",
        placeholder="Digite o curso",
        key="categoria",
        help="Digite o curso"
    )
    aula_index = st.number_input(
        label="Aula",
        placeholder="Índice da Aula",
        key="aula_index",
        help="Digite o índice da aula",
        step=int(1)
    )
    aula_modulo = st.number_input(
        label="Módulo",
        placeholder="Módulo da Aula",
        key="aula_modulo",
        help="Digite o módulo da aula",
        step=int(1)
    )
    url_video = st.text_input(
        label="Url",
        placeholder="URL do vídeo",
        key="url_video",
        help="Digite a URL do vídeo"
    )
    resumo = st.text_area(
        label="Resumo",
        placeholder="Resumo da Aula",
        key="resumo",
        height=400,
        help="Digite o resumo da aula"
    )
    notas = st.text_input(
        label="Notas",
        placeholder="Anotações da aula",
        key="notas",
        help="Digite as anotações da aula"
    )
    if st.button("Cadastrar Curso", type="primary", use_container_width=True):
        if insert_data(
            nome_curso, categoria, aula_index, aula_modulo, url_video, resumo, notas
        ):
            st.success("Curso cadastrado com sucesso", icon="✅")
        else:
            st.error("Erro ao cadastrar curso", icon="❌")


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
        # First filter by category and sort by aula_modulo and aula_index
        filtered_df = df[df["categoria"] == categoria_selecionada].sort_values(
            by=["aula_modulo", "aula_index"])

        # Get unique sorted modules
        sorted_modulos = filtered_df["aula_modulo"].unique()

        for modulo in sorted_modulos:
            # Filter aulas for current module and keep the sorting
            aulas = filtered_df[filtered_df["aula_modulo"] == modulo]
            with st.expander(f"Modulo: {modulo}", icon="📚"):
                for _, aula in aulas.iterrows():
                    st.write(
                        f":blue[Aula #{aula['aula_index']}] {
                            str(aula['nome_curso']).capitalize()}"
                    )
                    tab_aula, tab_resumo, tab_notas = st.tabs(
                        ["Aula", "Resumo", "Notas"])
                    with tab_aula:
                        st_player(aula["url_video"])
                        st.markdown("---")
                    with tab_resumo:
                        st.markdown(aula["resumo"], help="Resumo da aula")
                        st.markdown("---")
                    with tab_notas:
                        st.code(aula["notas"], language="html")
                        st.write("---")
    except:
        st.error("Erro ao carregar módulos do curso", icon="❌")
