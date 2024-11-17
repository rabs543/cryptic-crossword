FROM python:3.12
COPY src .
COPY pyproject.toml .
RUN pip install .
CMD ["python", "-m", "crosswords"]