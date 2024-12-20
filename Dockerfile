# Use uma imagem base leve com Python
FROM python:3.9-slim

EXPOSE 8080
WORKDIR /app

# Copie os arquivos de dependências para o contêiner
COPY requirements.txt requirements.txt

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Comando para iniciar o Streamlit no contêiner
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.enableCORS=false"]


