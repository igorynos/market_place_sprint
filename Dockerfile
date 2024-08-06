FROM python:latest

ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONPATH=/usr/src/market_place_sprint

WORKDIR /usr/src/market_place_sprint

COPY pyproject.toml poetry.lock* /usr/src/market_place_sprint/
RUN pip install poetry && poetry install --no-root

EXPOSE 8000

COPY . /usr/src/market_place_sprint

CMD ["python", "app/main.py"]