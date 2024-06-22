FROM python:3.8-slim

# Crie o usuário willians_seo com UID 1001 e GID 1002
RUN groupadd -g 1002 willians_seo && useradd -u 1001 -g willians_seo -ms /bin/bash willians_seo

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
COPY ./app /app

# Mude para o usuário willians_seo
USER willians_seo

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

