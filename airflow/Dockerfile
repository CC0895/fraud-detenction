FROM apache/airflow:2.6.3-python3.10

# Passiamo al root per installare pacchetti di sistema
USER root

RUN apt-get update \
    && apt-get install -y \
       vim \
       curl \
       netcat \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copiamo il file requirements.txt e lo installiamo come utente airflow
COPY requirements.txt /requirements.txt

# Passiamo all'utente airflow prima di eseguire pip
USER airflow

RUN pip install --no-cache-dir -r /requirements.txt

RUN mkdir -p /opt/airflow/dags /opt/airflow/logs /opt/airflow/plugins

ENV AIRFLOW_HOME=/opt/airflow

# Passiamo di nuovo a root per creare il gruppo airflow e cambiare permessi
USER root

# Creiamo il gruppo airflow se non esiste
RUN groupadd airflow

# Cambiamo i permessi della cartella
RUN chown -R airflow:airflow $AIRFLOW_HOME

# Passiamo a airflow per creare l'utente admin
USER airflow

# Comando di default per avviare il Webserver e lo Scheduler
CMD ["bash", "-c", "airflow db init && airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com --password admin && airflow webserver & airflow scheduler"]
