FROM python:latest
LABEL Davi Segundo
COPY . /var/www
WORKDIR /var/www
RUN pip install -r requirements.txt
ENTRYPOINT python ciencia_de_dados_equipe_3_trabalho_final.py