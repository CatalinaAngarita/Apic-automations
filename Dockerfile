FROM python:3.11-slim

WORKDIR /code

# Esta línea es la solución mágica para errores de importación
ENV PYTHONPATH=/code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el contenido de app a /code/app
COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]