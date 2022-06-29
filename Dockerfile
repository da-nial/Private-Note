FROM m.docker-registry.ir/python:3.9-slim AS compile-image
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY Back/setup.py .
COPY Back/ .
RUN pip install -e .


FROM m.docker-registry.ir/python:3.9-slim AS build-image
COPY --from=compile-image /opt/venv /opt/venv

RUN . /opt/venv/bin/activate

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
ENV FLASK_APP='pvnoteflask'
