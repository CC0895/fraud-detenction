FROM python:3.10-slim

# Imposta la cartella di lavoro
WORKDIR /app

# Copia il file requirements.txt
COPY requirements.txt /app

# Installa le dipendenze Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutta l'applicazione
COPY . /app

# Comando di esecuzione corretto
CMD ["pyway", "migrate"]
