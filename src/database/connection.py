from supabase import create_client, Client
from supabase.client import ClientOptions
import streamlit as st
import pandas as pd


supabase_url = st.secrets["SUPABASE_URL"]
supabase_key = st.secrets["SUPABASE_API_KEY"]
supabase: Client = create_client(
    supabase_url,
    supabase_key,
    options=ClientOptions(
        postgrest_client_timeout=20,
        storage_client_timeout=20,
        schema="public",
    ),
)
DATABASE = st.secrets["SUPABASE_DB"]


def insert_data(
    nome_curso, categoria, aula_index, aula_modulo, url_video, resumo, notas
):
    """
    Insere dados no banco de dados.

    Esta função insere um novo registro na tabela especificada do banco de dados Supabase.

    Parâmetros:
        nome_curso (str): O nome do curso.
        categoria (str): A categoria do curso.
        aula_index (int): O índice da aula.
        aula_modulo (str): O módulo da aula.
        url_video (str): A URL do vídeo da aula.
        resumo (str): Um resumo do conteúdo da aula.
        notas (str): Notas adicionais.

    Retorna:
        response: A resposta da operação de inserção, caso seja bem-sucedida.
    """
    try:
        response = (
            supabase.table(DATABASE)
            .insert(
                {
                    "nome_curso": nome_curso,
                    "categoria": categoria,
                    "aula_index": aula_index,
                    "aula_modulo": aula_modulo,
                    "url_video": url_video,
                    "resumo": resumo,
                    "notas": notas,
                }
            )
            .execute()
        )
        if response.data:
            return response
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}", icon="❌")


@st.cache_data
def get_all_data():
    """
    Recupera todos os dados da tabela especificada no banco de dados.
    Esta função é cacheada usando o decorador cache_data do Streamlit para melhorar o desempenho
    armazenando os resultados em memória.

    Retorna:
        pandas.DataFrame: Um DataFrame contendo todos os dados do banco de dados com as seguintes colunas:
            - nome_curso: Nome do curso
            - categoria: Categoria
            - url_video: URL do vídeo
            - aula_index: Índice da aula
            - aula_modulo: Módulo da aula
            - resumo: Resumo
            - notas: Anotações

        Retorna um DataFrame vazio se:
            - Nenhum dado for encontrado no banco de dados
            - Ocorrer um erro durante a conexão com o banco de dados

    Exceções:
        Exception: Captura e trata quaisquer exceções que ocorram durante as operações do banco de dados,
                exibindo a mensagem de erro através do componente de erro do Streamlit.

    Notas:
        - Utiliza Supabase como backend do banco de dados
        - O nome da tabela do banco de dados é especificado pela constante DATABASE
        - Exibe mensagens de erro usando o componente de erro do Streamlit
    """
    try:
        response = (
            supabase.table(DATABASE)
            .select(
                "nome_curso, categoria, url_video, aula_index, aula_modulo, url_video, resumo, notas"
            )
            .execute()
        )

        if response.data:
            df = pd.DataFrame(response.data)
            return df
        else:
            st.error(
                "Erro ao obter dados do banco de dados: Nenhum dado retornado.",
                icon="❌",
            )
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}", icon="❌")
        return pd.DataFrame()
