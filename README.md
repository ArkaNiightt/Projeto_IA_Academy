<p align="center">
	<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">PROJETO_IA_ACADEMY</h1></p>
<p align="center">
	<em>Empoderando o Aprendizado através de Módulos de IA Interativos</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/ArkaNiightt/Projeto_IA_Academy?style=default&logo=opensourceinitiative&logoColor=white&color=003fff" alt="license">
	<img src="https://img.shields.io/github/last-commit/ArkaNiightt/Projeto_IA_Academy?style=default&logo=git&logoColor=white&color=003fff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/ArkaNiightt/Projeto_IA_Academy?style=default&color=003fff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/ArkaNiightt/Projeto_IA_Academy?style=default&color=003fff" alt="repo-language-count">
</p>
<p align="center"><!-- opção padrão, sem badges de dependência. -->
</p>
<p align="center">
	<!-- opção padrão, sem badges de dependência. -->
</p>
<br>

## 🔗 Índice

- [📍 Visão Geral](#-visão-geral)
- [👾 Funcionalidades](#-funcionalidades)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
  - [📂 Índice do Projeto](#-índice-do-projeto)
- [🚀 Começando](#-começando)
  - [☑️ Pré-requisitos](#-pré-requisitos)
  - [⚙️ Instalação](#-instalação)
  - [🤖 Uso](#-uso)
  - [🧪 Testes](#-testes)
- [📌 Roteiro do Projeto](#-roteiro-do-projeto)
- [🔰 Contribuindo](#-contribuindo)
- [🎗 Licença](#-licença)
- [🙌 Agradecimentos](#-agradecimentos)

---

## 📍 Visão Geral

ProjetoIAAcademy é uma plataforma de aprendizado interativo projetada para simplificar a jornada educacional para entusiastas de tecnologia. Ela oferece uma interface amigável para explorar módulos de cursos categorizados, completos com aulas em vídeo, resumos de conteúdo e notas de aula. Com autenticação robusta de usuários e cumprimentos personalizados, a plataforma garante uma experiência de aprendizado segura e personalizada. Ideal para autodidatas e estudantes de tecnologia, ela simplifica o processo de acesso e digestão de conteúdo técnico complexo.

---

## 👾 Funcionalidades

|      | Funcionalidade    | Resumo       |
| :--- | :---:             | :---         |
| ⚙️  | **Arquitetura**    | <ul><li>Utiliza uma arquitetura modular com arquivos separados para diferentes funcionalidades.</li><li>Ponto de entrada principal é `app.py` no diretório `src`.</li><li>A conexão com o banco de dados é gerenciada por `connection.py` no diretório `src/database`.</li></ul> |
| 🔩 | **Qualidade de Código** | <ul><li>O código é organizado e modular, facilitando a compreensão e manutenção.</li><li>Tratamento de exceções implementado na conexão com o banco de dados.</li></ul> |
| 📄 | **Documentação** | <ul><li>Principal linguagem utilizada é Python.</li><li>Comandos de instalação, uso e testes estão bem documentados.</li></ul> |
| 🔌 | **Integrações** | <ul><li>Integrado com `pip` para gerenciamento de pacotes.</li><li>Utiliza `Supabase` para gerenciamento de banco de dados.</li><li>Configurações OAuth2 para Google e Microsoft estão configuradas.</li></ul> |
| 🧩 | **Modularidade** | <ul><li>O código está dividido em módulos separados para diferentes funcionalidades.</li><li>Cada módulo é responsável por uma tarefa específica, melhorando a legibilidade e manutenção.</li></ul> |
| 🧪 | **Testes** | <ul><li>Comandos de teste são fornecidos na documentação.</li><li>Utiliza `pytest` para testes.</li></ul> |
| ⚡️  | **Desempenho**   | <ul><li>Conexão eficiente com o banco de dados e recuperação de dados usando `pandas DataFrame`.</li><li>Interface de usuário interativa com `Streamlit` para melhor experiência do usuário.</li></ul> |
| 🛡️ | **Segurança**    | <ul><li>Autenticação segura de usuários e gerenciamento de sessões.</li><li>Configurações OAuth2 para Google e Microsoft aumentam a segurança.</li><li>Emails pré-autorizados são gerenciados no arquivo de configuração.</li></ul> |
| 📦 | **Dependências** | <ul><li>Dependências são gerenciadas usando `pip` e listadas em `requirements.txt`.</li><li>Projeto utiliza Python e outras bibliotecas listadas em `requirements.txt`.</li></ul> |
| 🚀 | **Escalabilidade** | <ul><li>Estrutura de código modular permite fácil escalabilidade.</li><li>Arquivo de configuração permite fácil gerenciamento das configurações à medida que o projeto escala.</li></ul> |

---

## 📁 Estrutura do Projeto

```sh
└── Projeto_IA_Academy/
	├── config
	│   └── config.yaml
	├── requirements.txt
	└── src
		├── academy.py
		├── app.py
		└── database
```

### 📂 Índice do Projeto
<details open>
	<summary><b><code>PROJETO_IA_ACADEMY/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/ArkaNiightt/Projeto_IA_Academy/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>- O arquivo 'requirements.txt' descreve as dependências necessárias para o projeto<br>- Ele lista versões específicas de bibliotecas e pacotes necessários para garantir que o projeto funcione conforme o esperado<br>- Isso inclui bibliotecas para desenvolvimento web, processamento de dados, segurança e mais, proporcionando uma configuração de ambiente abrangente para o projeto.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- src Submodule -->
		<summary><b>src</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/ArkaNiightt/Projeto_IA_Academy/blob/master/src/academy.py'>academy.py</a></b></td>
				<td>- O arquivo 'academy.py' no diretório 'src' é responsável por carregar e exibir módulos de cursos organizados por categoria em uma interface Streamlit<br>- Ele fornece uma interface de usuário interativa para selecionar categorias, visualizar módulos expansíveis e acessar aulas individuais com players de vídeo, resumos de conteúdo e notas de aula em formato de código.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/ArkaNiightt/Projeto_IA_Academy/blob/master/src/app.py'>app.py</a></b></td>
				<td>- App.py serve como o ponto de entrada principal para a aplicação IA - Academy<br>- Ele gerencia a autenticação de usuários, incluindo funcionalidades de login, logout e redefinição de senha<br>- Além disso, ele lida com cumprimentos específicos de usuário e carrega módulos com base no estado da sessão do usuário<br>- A configuração da aplicação é carregada a partir de um arquivo YAML.</td>
			</tr>
			</table>
			<details>
				<summary><b>database</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/ArkaNiightt/Projeto_IA_Academy/blob/master/src/database/connection.py'>connection.py</a></b></td>
						<td>- O connection.py no diretório src/database estabelece uma conexão com o banco de dados Supabase, recupera todos os dados de uma tabela específica e os retorna como um pandas DataFrame<br>- Ele também lida com exceções e exibe mensagens de erro usando o componente de erro do Streamlit.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- config Submodule -->
		<summary><b>config</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/ArkaNiightt/Projeto_IA_Academy/blob/master/config/config.yaml'>config.yaml</a></b></td>
				<td>- Config/config.yaml serve como um arquivo de configuração central para o projeto, gerenciando configurações de cookies, credenciais de usuários, configurações OAuth2 para Google e Microsoft, e emails pré-autorizados<br>- Ele desempenha um papel crucial na autenticação de usuários, autorização e gerenciamento de sessões, contribuindo para a segurança e funcionalidade geral da aplicação.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## 🚀 Começando

### ☑️ Pré-requisitos

Antes de começar com o Projeto_IA_Academy, certifique-se de que seu ambiente de execução atende aos seguintes requisitos:

- **Linguagem de Programação:** Python
- **Gerenciador de Pacotes:** Pip

### ⚙️ Instalação

Instale o Projeto_IA_Academy usando um dos seguintes métodos:

**Construir a partir do código-fonte:**

1. Clone o repositório Projeto_IA_Academy:
```sh
❯ git clone https://github.com/ArkaNiightt/Projeto_IA_Academy
```

2. Navegue até o diretório do projeto:
```sh
❯ cd Projeto_IA_Academy
```

3. Instale as dependências do projeto:

**Usando `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```

### 🤖 Uso
Execute o Projeto_IA_Academy usando o seguinte comando:
**Usando `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```

### 🧪 Testes
Execute a suíte de testes usando o seguinte comando:
**Usando `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```

---

## 📌 Roteiro do Projeto

- [X] **`Tarefa 1`**: <strike>Implementar a funcionalidade um.</strike>
- [ ] **`Tarefa 2`**: Implementar a funcionalidade dois.
- [ ] **`Tarefa 3`**: Implementar a funcionalidade três.

---

## 🔰 Contribuindo

- **💬 [Participe das Discussões](https://github.com/ArkaNiightt/Projeto_IA_Academy/discussions)**: Compartilhe seus insights, forneça feedback ou faça perguntas.
- **🐛 [Reportar Problemas](https://github.com/ArkaNiightt/Projeto_IA_Academy/issues)**: Envie bugs encontrados ou registre pedidos de funcionalidades para o projeto `Projeto_IA_Academy`.
- **💡 [Enviar Pull Requests](https://github.com/ArkaNiightt/Projeto_IA_Academy/blob/main/CONTRIBUTING.md)**: Revise PRs abertas e envie suas próprias PRs.

<details closed>
<summary>Diretrizes de Contribuição</summary>

1. **Fork do Repositório**: Comece forkeando o repositório do projeto para a sua conta no GitHub.
2. **Clone Localmente**: Clone o repositório forked para sua máquina local usando um cliente Git.
   ```sh
   git clone https://github.com/ArkaNiightt/Projeto_IA_Academy
   ```
3. **Crie um Novo Branch**: Sempre trabalhe em um novo branch, dando um nome descritivo.
   ```sh
   git checkout -b nova-funcionalidade-x
   ```
4. **Faça Suas Alterações**: Desenvolva e teste suas alterações localmente.
5. **Comite Suas Alterações**: Comite com uma mensagem clara descrevendo suas atualizações.
   ```sh
   git commit -m 'Implementada nova funcionalidade x.'
   ```
6. **Push para o GitHub**: Envie as alterações para seu repositório forked.
   ```sh
   git push origin nova-funcionalidade-x
   ```
7. **Envie um Pull Request**: Crie um PR contra o repositório original do projeto. Descreva claramente as mudanças e suas motivações.
8. **Revisão**: Uma vez que seu PR for revisado e aprovado, ele será mesclado no branch principal. Parabéns pela sua contribuição!
</details>

<details open>
<summary>Gráfico de Contribuidores</summary>
<br>
<p align="left">
   <a href="https://github.com/ArkaNiightt/Projeto_IA_Academy/graphs/contributors">
	  <img src="https://contrib.rocks/image?repo=ArkaNiightt/Projeto_IA_Academy">
   </a>
</p>
</details>

---
