# IA - Academy

![Badge](https://img.shields.io/badge/Python-3.10-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## Descrição

**IA - Academy** é uma aplicação desenvolvida em Python utilizando o framework Streamlit. O projeto tem como objetivo oferecer uma plataforma interativa para cadastrar, organizar e visualizar cursos, módulos e aulas com suporte a vídeos e resumos. A aplicação utiliza Supabase como backend para gerenciamento de dados e autenticação de usuários com diferentes níveis de acesso.

## Funcionalidades

- **Autenticação de Usuários**: Login seguro com suporte a múltiplos usuários e níveis de permissão (admin, editor, viewer).
- **Cadastro de Cursos**: Interface para adicionar novos cursos, categorias, módulos e aulas.
- **Visualização de Módulos**: Navegação intuitiva por categorias e módulos, com acesso a vídeos e resumos das aulas.
- **Armazenamento Seguro**: Utilização do Supabase para armazenamento e gerenciamento de dados.
- **Interface Intuitiva**: Design responsivo e fácil de usar construída com Streamlit.

## Tecnologias Utilizadas

- **Python 3.10**
- **Streamlit**: Framework para construção de aplicações web interativas.
- **Supabase**: Backend como serviço para gerenciamento de banco de dados.
- **Streamlit Authenticator**: Biblioteca para autenticação de usuários.
- **Pandas**: Manipulação e análise de dados.
- **Streamlit Player**: Integração de players de vídeo na interface.

## Instalação

1. **Clone o repositório**

 ```bash
 git clone https://github.com/ArkaNiightt/Projeto_IA_Academy.git
 cd IA-Academy
 ```

2. **Crie um ambiente virtual**

 ```bash
 python -m venv venv
 source venv/bin/activate  # No Windows use `venv\Scripts\activate`
 ```

3. **Instale as dependências**

 ```bash
 pip install -r requirements.txt
 ```

## Configuração

1. **Configure as variáveis de ambiente**

 Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:

 ```env
 SUPABASE_URL=your_supabase_url
 SUPABASE_API_KEY=your_supabase_api_key
 SUPABASE_DB=your_database_name
 ```

2. **Configure as credenciais de autenticação**

 Edite o arquivo `config/config.yaml` com as informações dos usuários:

```yaml
 cookie:
   expiry_days: 30
   key: your_cookie_key
   name: your_cookie_name
 credentials:
   usernames:
   usuario1:
   email: usuario1@example.com
   password: hashed_password
   first_name: Nome
   last_name: Sobrenome
   roles:
   - admin
 oauth2:
   google:
   client_id: your_google_client_id
   client_secret: your_google_client_secret
   redirect_uri: your_redirect_uri
   microsoft:
   client_id: your_microsoft_client_id
   client_secret: your_microsoft_client_secret
   redirect_uri: your_redirect_uri
   tenant_id: your_tenant_id
 pre-authorized:
   emails: null
```

## Uso

1. **Execute a aplicação**

 ```bash
 streamlit run src/app.py
 ```

2. **Acesse a aplicação**

 Abra o navegador e vá para `http://localhost:8501`.

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. **Fork este repositório**
2. **Crie uma branch para sua feature**

 ```bash
 git checkout -b minha-feature
 ```

3. **Commit suas mudanças**

 ```bash
 git commit -m "Adiciona nova feature"
 ```

4. **Push para a branch**

 ```bash
 git push origin minha-feature
 ```

5. **Abra um Pull Request**

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
