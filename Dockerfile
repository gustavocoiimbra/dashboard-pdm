FROM python:3.9-slim
EXPOSE 8080
WORKDIR /app

# Copie os arquivos de dependências para o contêiner
COPY requirements.txt requirements.txt

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie o resto dos arquivos da aplicação
COPY . .

# Configure as variáveis de ambiente do Streamlit
ENV STREAMLIT_SERVER_PORT=8080
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Comando para iniciar o Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0", "--server.enableCORS=false"]


