
# **Projeto de Backend**

## **Visão Geral**

Este projeto foi desenvolvido como parte de um exercício prático para aprimorar habilidades em **desenvolvimento backend**, utilizando o framework **FastAPI** em Python. 

---

## **Funcionalidades**

- **Criação de uma publicação**
- **Modificação de uma publicação**
- **Listagem de publicações**
- **Deleção de uma publicação**
- **Criação de hash das publicações**
- **Compactação das publicações**

---

## **Tecnologias**

- **Python** (versão 3.12)
- **FastAPI**  
- **Pandas**  

---

## **Instalação e Uso**

### **Pré-requisitos**

- **UV**: uma ferramenta para gerenciar ambientes e dependências no Python.  
  Siga os passos abaixo para instalar e configurar.

---

### **Instalação do UV**

- **Windows**: Execute o seguinte comando no PowerShell:
  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

- **Linux ou macOS**: Execute o comando:
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

---

### **Clonando o Repositório**
1. Clone o repositório para sua máquina local:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd <NOME_DA_PASTA>
   ```

---

### **Configurando o Ambiente Virtual**
1. Crie o ambiente virtual usando o UV:
   ```bash
   uv venv --python 3.12
   ```

2. Ative o ambiente virtual:
   - **Windows**:
     ```bash
     .venv\Scripts\Activate
     ```
   - **Linux ou macOS**:
     ```bash
     source .venv/bin/activate
     ```

3. Adicione as dependências necessárias:
   ```bash
   uv add fastapi[standard]
   uv add pandas
   ```

---

### **Executando o Projeto**
1. Inicie o servidor de desenvolvimento do FastAPI:
   ```bash
   fastapi dev .\main.py
   ```
2. O servidor estará disponível no endereço:
   ```
   http://127.0.0.1:8000
   ```
