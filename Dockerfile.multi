FROM m.docker-registry.ir/python:3.9-slim AS compile-image
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src .
RUN pip install .


FROM m.docker-registry.ir/python:3.9-slim AS build-image
COPY --from=compile-image /opt/venv /opt/venv

RUN . /opt/venv/bin/activate

ENV PATH="/opt/venv/bin:$PATH"
ENV FLASK_APP='privatenote'
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]
